
let url = window.location.protocol + '//' + window.location.host
let path = url + '/trabalhos/detalhe/mapa/json/'
let busca = window.location.search
split = busca.split('&')
trabalho = split[0].split('=')[1]

var pontosRota = []

$(document).ready(function(){
  initMap()
})

var Areas = []
var Trajeto = []
var Polyline = null
var listenerDragend
var listenerBounds
var listenerZoom
var centro

class Marcador extends google.maps.Marker {

  posicao;

  constructor(mapOptions, posicao){
    super(mapOptions)
    this.posicao = posicao
  }

}

function initMap(){

  var mapOptions = {
    center: { lat: -9.37975, lng: -40.501976 },
    zoom: 19,
    minZoom:17,
    streetViewControl: false,
    /* mapTypeId: google.maps.MapTypeId.SATELLITE, */

  }
  
  maps = new google.maps.Map(document.getElementById('map'), mapOptions)

  const centerControlDiv = document.createElement("div")
  const rightControlDiv = document.createElement('div');
  ControleVoltarMap(centerControlDiv, maps);
  maps.controls[google.maps.ControlPosition.LEFT_CENTER].push(centerControlDiv);

  ControleRotaMap(rightControlDiv, maps)
  maps.controls[google.maps.ControlPosition.RIGHT_CENTER].push(rightControlDiv)
  
  listenerBounds = google.maps.event.addListener(maps, "bounds_changed", bounds_changed)
  listenerDragend = google.maps.event.addListener(maps, "dragend", bounds_changed)
  listenerZoom = google.maps.event.addListener(maps, "zoom_changed", bounds_changed) 

}

function bounds_changed(){
  
  zoom = maps.getZoom()

    let ne = maps.getBounds().getNorthEast()
    let sw = maps.getBounds().getSouthWest()

    
    p1 = {'lat':ne.lat(), 'lng':sw.lng()}

    p2 = {'lat':ne.lat(), 'lng':ne.lng()}
    
    p3 = {'lat':sw.lat(), 'lng':sw.lng()}
    
    p4 = {'lat':sw.lat(), 'lng':ne.lng()}

    mapa_visivel = [p1, p2, p4, p3]    
    
    getDados(JSON.stringify(mapa_visivel), zoom, maps)

}


function getDados(mapavisivel, zoom, map){

  let dados

  $.ajax({
    type:"POST",
    url:path,
    cache:false,
    data:{
        'trabalho':trabalho,
        'mapavisivel':mapavisivel,
        'zoom':zoom        
    },
    success: function(response){
           
      google.maps.event.removeListener(listenerZoom)
      google.maps.event.removeListener(listenerDragend)
      limparMapa()
      let trabalho = response['trabalho']
      if(centro == null){
        google.maps.event.removeListener(listenerBounds)
        centro = {'lat':trabalho[0]['lat'], 'lng':trabalho[0]['lng']}
        map.setCenter(centro)
      }
      CriarAreas(response['areas'], map)
      polyline = Trajego(trabalho, map)
      Poly(polyline, map)
      listenerDragend = google.maps.event.addListener(maps, "dragend", bounds_changed)
      listenerZoom = google.maps.event.addListener(maps, "zoom_changed", bounds_changed)
     
    }
  })

return dados

}


function CriarAreas(areas, map){
  
    for(var i=0; i < areas.length; i++)
    {
      construirArea(areas[i], maps)
    }
}


function construirArea(area, map, index){
    let a = {}
    let nome = area['nome']
    const centro = area['centro']

      
    let window = InfoWindow(nome)
  
    let marker = new google.maps.Marker({
      position: centro,
      map,
      icon:'http://maps.google.com/mapfiles/ms/icons/red-dot.png'  
    })

    a['centro'] = marker
  
    marker.addListener('click', () =>{
      window.open({
        anchor: marker,
        map,
        shouldFocus: true
      })
    })
    let vertices = area['vertices']
    let polygon = new google.maps.Polygon({
      paths:vertices,
      strokeColor: '#FF0000',
      strokeOpacity: 0.5,
      strokeWeight:2,
      fillColor: '#FF0000',
      fillOpacity:0.35,
      map,
    })

    a['vertices'] = polygon  
  
    let ruas = area['ruas']
    let salvar_ruas = []
    ruas.forEach(rua => {
      let nome = rua['nome']
      let pontos = rua['pontos']
        pontos.forEach(ponto =>{
  
          let window = InfoWindow(nome)
          
          let marker = new google.maps.Marker({
            position:ponto,
            map,
            icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
          })

          salvar_ruas.push(marker)
  
          marker.addListener('click', () =>{
            window.open({
              anchor:marker,
              map,
              shouldFocus: true
            })
          })
  
        })
    })
    a['ruas'] = salvar_ruas

    Areas.push(a)
  
}


function InfoWindow(texto){
    let window = new google.maps.InfoWindow({
      content: "<h5>"+ texto +"</h5>"
    })
  
    return window
  }
  
  function ControleVoltarMap(controlDiv, map) {
  
    const controlVoltar = document.createElement("div")
  
    controlVoltar.style.backgroundColor = "#fff";
    controlVoltar.style.border = "2px solid #fff";
    controlVoltar.style.borderRadius = "3px";
    controlVoltar.style.boxShadow = "0 2px 6px rgba(0,0,0,.3)";
    controlVoltar.style.cursor = "pointer";
    controlVoltar.style.marginTop = "8px";
    controlVoltar.style.marginBottom = "22px";
    controlVoltar.style.textAlign = "center";
    controlVoltar.title = "Voltar para a lista de áreas";
    controlDiv.appendChild(controlVoltar)
  
    const controlTextVoltar = document.createElement("div");
  
    controlTextVoltar.style.color = "rgb(25,25,25)";
    controlTextVoltar.style.fontFamily = "Roboto,Arial,sans-serif";
    controlTextVoltar.style.fontSize = "16px";
    controlTextVoltar.style.lineHeight = "38px";
    controlTextVoltar.style.paddingLeft = "5px";
    controlTextVoltar.style.paddingRight = "5px";
    controlTextVoltar.innerHTML = "Voltar";
    controlVoltar.appendChild(controlTextVoltar);
    // Limpar polylines no mapa
    controlVoltar.addEventListener("click", () => {
        window.history.go(-1)
    });


    
    
}


function ControleRotaMap(controlDiv, map) {

  const controlInicioRota = document.createElement("div")
  
  controlInicioRota.style.backgroundColor = "#fff";
  controlInicioRota.style.border = "2px solid #fff";
  controlInicioRota.style.borderRadius = "3px";
  controlInicioRota.style.boxShadow = "0 2px 6px rgba(0,0,0,.3)";
  controlInicioRota.style.cursor = "pointer";
  controlInicioRota.style.marginTop = "8px";
  controlInicioRota.style.marginBottom = "22px";
  controlInicioRota.style.textAlign = "center";
  
  controlDiv.appendChild(controlInicioRota)

  controlInicioRota.addEventListener("click",()=>{

    if(pontosRota.length >= 2){

      let pontos = []

      let nome_rota = window.prompt('Qual o nome da rota?')

      for(let i =0; i<pontosRota.length; i++){
        pontos.push(pontosRota[i].posicao)
      }

      rota = {
            'nome': nome_rota,
            'rota': pontos
          }

      _json = JSON.stringify(rota)
      
      let url = window.location.protocol + '//' + window.location.host + '/areas/rota/adicionar'
      console.log(url)
      $.ajax({
        type:"POST",
        cache:false,
        url:url,
        data:{
          'rota':_json
        },
        success:function(response){
          window.alert('Rota salva com sucesso')
          
        }

      })
      
    }
    else{
      window.alert('Selecione o início e o final da rota')
    }

  })

  const controlTextInicio = document.createElement("div");

  controlTextInicio.style.color = "rgb(25,25,25)";
  controlTextInicio.style.fontFamily = "Roboto,Arial,sans-serif";
  controlTextInicio.style.fontSize = "16px";
  controlTextInicio.style.lineHeight = "38px";
  controlTextInicio.style.paddingLeft = "5px";
  controlTextInicio.style.paddingRight = "5px";
  controlTextInicio.innerHTML = "Enviar Rota";
  controlInicioRota.appendChild(controlTextInicio);

  
}

function Trajego(trajeto, map){
    polyline = []
    

    for(var i=0; i < trajeto.length; i++){
        posicao = trajeto[i]
        position = {lat:Number(posicao['lat']), lng:Number(posicao['lng'])}
        polyline.push(position)
        let marker = null
        
        marker = new Marcador({
                  position:position,
                  map:map,
                  icon: {
                    path: google.maps.SymbolPath.CIRCLE,
                    scale: 4,
                  } 
            }, posicao)

        let infoWindow = new google.maps.InfoWindow({
            content: "<h4>Horário: "+posicao.horario+"</h4><p><h4>Lat: "+posicao['lat']+"</h4>"
        })

        google.maps.event.addListener(infoWindow, 'closeclick', function(){
          console.log('infowindow closeclick')
        })

        marker.addListener("click", () =>{
     
            infoWindow.open({
              anchor:marker,
              map:map,               
              shouldFocus:true
          })

        })

        google.maps.event.addListener(marker, 'dblclick', function (){
          icon = marker.getIcon()
          if(icon == 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'){
            marker.setIcon({
              path: google.maps.SymbolPath.CIRCLE,
              scale: 4,
            })
            removeSelecao(marker)

          }
          else{
            marker.setIcon('http://maps.google.com/mapfiles/ms/icons/blue-dot.png')
            addSelecao(marker)
          }
          
          

        })
        
       
      
      Trajeto.push(marker)
    }

    

    return polyline
}

function addSelecao(marcador){
  let contem_marcador = false
  console.log(pontosRota.length)
  if(pontosRota.length < 2){
    

    for(var i =0; i< pontosRota.length; i++){
      t_marcador = pontosRota[i]

      if (t_marcador.posicao['id'] == marcador.posicao['id']){
          contem_marcador = true
          break
      }
    }
    if(!contem_marcador){
      pontosRota.push(marcador)
    }
    else{
      alert('Marcador já incluso')
    }
  }

  return !contem_marcador
}

function removeSelecao(marcador){
  for(var i=0; i< pontosRota.length; i++){
    t_marcador = pontosRota[i]

    if(t_marcador.posicao['id'] == marcador.posicao['id'])
    {
      pontosRota.splice(i, 1)
    }
  }
}

function Poly(pontos, map){

    const path = new google.maps.Polyline({
        map:map,
        path: pontos,
        geodesic: true,
        strokeColor: "#FF0000",
        strokeOpacity: 1.0,
        strokeWeight: 2,
      });

   Polyline = path 
}

function Imagens(imagens){
  
  imagens.forEach(function(imagem){

    const pontos = {
      north: imagem['north'],
      south:imagem['south'],
      east:imagem['east'],
      west:imagem['west']
    }
    
    img = url + '/imagens/exibir/' + imagem['id']
    
    overlay = new google.maps.GroundOverlay(
      img,
      pontos
    )
    overlay.setMap(map)

  })
}

function limparMapa() {    

    if(Areas.length > 0){
     
      let length = Areas.length

      for(var i=0; i<length; i++){
        centro = Areas[i]['centro']
        centro.setMap(null)
        vertices = Areas[i]['vertices']
        vertices.setMap(null)
        ruas =  Areas[i]['ruas']
        for(j=0; j< ruas.length;j++)
        {
          rua = ruas[j]
          rua.setMap(null)
        }   
      }

      Areas = []
    }

    if(Trajeto.length > 0)
    {
      for(var i = 0; i <Trajeto.length; i++){
        
        Trajeto[i].setMap(null)
      }
    }

    if(Polyline != null)
    {
      Polyline.setMap(null)
    }
    
  }




