
let url = window.location.protocol + '//' + window.location.host + '/areas/mapa/json/'
let busca = window.location.search

if(busca != ""){
  let id_area = window.location.search.split('=')[1]
  url =  url + id_area
}

var map

$.ajax({
  type: "GET",
  url:url,
  cache: true,
  success: function (response) {

    map = new google.maps.Map(document.getElementById("map"), {
      zoom: 18,
      streetViewControl:false,
    })

    const centerControlDiv = document.createElement("div");
    ControleMap(centerControlDiv, map);
    map.controls[google.maps.ControlPosition.LEFT_TOP].push(centerControlDiv);

    if(busca != ""){     
      let area = response['area'] 
      construirArea(area)
    }else{    
      let areas = response['areas']
      Areas(areas)
    }
    
  }
})

function Areas(areas){
  
  for(var i=0; i < areas.length; i++)
  {
    construirArea(areas[i])
  }

}


function construirArea(area){
  let nome = area['nome']
  const centro = area['centro']
  map.setCenter(centro)

  let window = InfoWindow(nome)

  let marker = new google.maps.Marker({
    position: centro,
    map,
    icon:'http://maps.google.com/mapfiles/ms/icons/red-dot.png'  
  })

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

  let ruas = area['ruas']
  console.log(ruas)

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

        marker.addListener('click', () =>{
          window.open({
            anchor:marker,
            map,
            shouldFocus: true
          })
        })

      })
  });

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





  