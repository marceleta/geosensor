
let url = window.location.protocol + '//' + window.location.host
let path = url + '/trabalhos/detalhe/mapa/json/'
let busca = window.location.search
split = busca.split('&')
trabalho = split[0].split('=')[1]
h_inicio = split[1].split('=')[1]
h_final = split[2].split('=')[1]

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

function initMap(){

  var mapOptions = {
    center: { lat: -9.37975, lng: -40.501976 },
    zoom: 19,
    minZoom:17,
    streetViewControl: false,
    /* mapTypeId: google.maps.MapTypeId.SATELLITE, */

  }
  
  maps = new google.maps.Map(document.getElementById('map'), mapOptions)

  const centerControlDiv = document.createElement("div");
  ControleMap(centerControlDiv, maps);
  maps.controls[google.maps.ControlPosition.LEFT_CENTER].push(centerControlDiv);
  
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
        'hinicio':h_inicio,
        'hfinal':h_final,
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
  
  function ControleMap(controlDiv, map) {
  
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


function Trajego(trajeto, map){
    polyline = []
    

    for(var i=0; i < trajeto.length; i++){
        posicao = trajeto[i]
        position = {lat:Number(posicao['lat']), lng:Number(posicao['lng'])}
        polyline.push(position)
        let marker = null
        if (i == 0){
                marker = new google.maps.Marker({
                position:position,
                map:map,
                icon: 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
            })
        }else if(i==(trajeto.length-1)){
                marker = new google.maps.Marker({
                position:position,
                map:map,
                icon: 'http://maps.google.com/mapfiles/ms/icons/orange-dot.png'
            })
        }else{
                marker = new google.maps.Marker({
                position:position,
                map:map,
                icon: {
                    path: google.maps.SymbolPath.CIRCLE,
                    scale: 4,
                } 
            })
        }

        let infoWindow = new google.maps.InfoWindow({
            content: "<h6>Horário: "+posicao.horario+"</h6><p><h6>Velocidade: "+posicao.velocidade+" Km/h</h6>",
        })


        marker.addListener("click", () =>{
            infoWindow.open({
                anchor:marker,
                map:map,               
                shouldFocus:true
            })
        }) 
      
      Trajeto.push(marker)
    }

    

    return polyline
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




