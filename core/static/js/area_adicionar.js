
$(document).ready(function(){
    initMap()
})

var tmp_polygon = []
var salvar_polygon = []

function initMap() {

    let mapOptions = {
        center: {lat: -9.37975, lng: -40.501976},
        zoom: 19,
        streetViewControl: false,
        /* mapTypeId: google.maps.MapTypeId.SATELLITE, */

    }


    map = new google.maps.Map(document.getElementById('map'), mapOptions)

    const centerControlDiv = document.createElement("div");
    ControleMap(centerControlDiv, map);
    map.controls[google.maps.ControlPosition.RIGHT_CENTER].push(centerControlDiv);
    drawing(map)

}

function drawing(map) {
        console.log('Drawing')
        var drawingManager = new google.maps.drawing.DrawingManager({
        drawingMode: google.maps.drawing.OverlayType.MARKER,
        drawingControl: true,
        drawingControlOptions: {
            position: google.maps.ControlPosition.TOP_CENTER,
            drawingModes: [
                google.maps.drawing.OverlayType.POLYGON,
            ],
        },
        markerOptions: {
            //Icon: "beachflag.png",
            editable:true,
            clickable:true,
            draggable: true,

        },
        polylineOptions: {
            strokeColor: "#000000",
            fillColor: "#ff0000",
            fillOpacity: 0.2,
            strokeWeight: 5,
            clickable: true,
            editable: true,
        },
        polygonOptions: {
            strokeColor: "#000000",
            //fillColor: "#000000",
            fillOpacity: 0.2,
            strokeWeight: 5,
            clickable: true,
            editable: true,
        },

    })
    drawingManager.setMap(map)
    google.maps.event.addListener(drawingManager, 'overlaycomplete', function (event) {
        switch (event.type) {
            case 'polygon': console.log('polygon')
                construirArea(event.overlay, map)
                break


        }

    })
}

function centroPolygon(polygon){
    let array = polygon.getPath().getArray()
    let bounds = new google.maps.LatLngBounds()

    for(let i= 0; i < array.length; i++){
        bounds.extend(array[i])
    }

    return bounds.getCenter()
}


function markerPolygon(latlng, map){

    let marker = new google.maps.Marker({
        position:latlng,
        map,
    })

    return marker
}


function construirArea(polygon, map){
    let centro = centroPolygon(polygon)
    let centro_marker = markerPolygon(centro, map)

    let nome_area = prompt('Qual o nome dessa área?')
    if(nome_area == null || nome_area == ""){
        let nome_area = prompt('Qual o nome dessa área?')
    }

    let text_window = "<h3>"+nome_area+"</h3>"
    let infowindow = new google.maps.InfoWindow({
        content:text_window
    })

    centro_marker.addListener("click", () => {
        infowindow.open({
            anchor:centro_marker,
            map:map,
            shouldFocus: false,
        })
    })

    area = {
        'centro': centro_marker,
        'polygon': polygon,
        'nome':nome_area,

    }

    tmp_polygon.push(area)

}

// Controle do mapa
function ControleMap(controlDiv, map) {

    const controlLimpar = document.createElement("div")

    controlLimpar.style.backgroundColor = "#fff";
    controlLimpar.style.border = "2px solid #fff";
    controlLimpar.style.borderRadius = "3px";
    controlLimpar.style.boxShadow = "0 2px 6px rgba(0,0,0,.3)";
    controlLimpar.style.cursor = "pointer";
    controlLimpar.style.marginTop = "8px";
    controlLimpar.style.marginBottom = "22px";
    controlLimpar.style.textAlign = "center";
    controlLimpar.title = "Limpar ultimo ponto";
    controlDiv.appendChild(controlLimpar)

    const controlTextLimpar = document.createElement("div");

    controlTextLimpar.style.color = "rgb(25,25,25)";
    controlTextLimpar.style.fontFamily = "Roboto,Arial,sans-serif";
    controlTextLimpar.style.fontSize = "16px";
    controlTextLimpar.style.lineHeight = "38px";
    controlTextLimpar.style.paddingLeft = "5px";
    controlTextLimpar.style.paddingRight = "5px";
    controlTextLimpar.innerHTML = "Limpar ultimo";
    controlLimpar.appendChild(controlTextLimpar);
    // Limpar polylines no mapa
    controlLimpar.addEventListener("click", () => {

        if(tmp_polygon.length > 0){
            p = tmp_polygon.pop()
            marker = p['centro']
            marker.setMap(null)

            polygon = p['polygon']
            polygon.setMap(null)

        }        
           
    })
    // controle para salvar os desenhos
    const controlSalvar = document.createElement("div")

    controlSalvar.style.backgroundColor = "#fff";
    controlSalvar.style.border = "2px solid #fff";
    controlSalvar.style.borderRadius = "3px";
    controlSalvar.style.boxShadow = "0 2px 6px rgba(0,0,0,.3)";
    controlSalvar.style.cursor = "pointer";
    controlSalvar.style.marginTop = "8px";
    controlSalvar.style.marginBottom = "22px";
    controlSalvar.style.textAlign = "center";
    controlSalvar.title = "Salvar pontos selecionados";
    controlDiv.appendChild(controlSalvar)

    const controlTextSalvar = document.createElement("div");

    controlTextSalvar.style.color = "rgb(25,25,25)";
    controlTextSalvar.style.fontFamily = "Roboto,Arial,sans-serif";
    controlTextSalvar.style.fontSize = "16px";
    controlTextSalvar.style.lineHeight = "38px";
    controlTextSalvar.style.paddingLeft = "5px";
    controlTextSalvar.style.paddingRight = "5px";
    controlTextSalvar.innerHTML = "Salvar";
    controlSalvar.appendChild(controlTextSalvar);

    controlTextSalvar.addEventListener("click", () => {

        if(tmp_polygon.length > 0){

            for(let i=0; i<=tmp_polygon.length; i++){
                p = tmp_polygon.pop()
    
                centro = p['centro']
                polygon = p['polygon']
                nome = p['nome']
    
                d = {
                    'centro':centro.position.toJSON(),
                    'vertices':polygon.getPath().getArray(),
                    'nome':nome
                }
    
                salvar_polygon.push(d)
    
            }

            area = {'areas':salvar_polygon}
            json = JSON.stringify(area)
            enviarDadosArea(json)

        }        
        else{

            window.alert('Desenhe a área no mapa antes de salvar')
        }
        
           
    })
}


function enviarDadosArea(dados){
    let url = window.location.protocol + '//' + window.location.host
    let path = url + '/areas/adicionar/mapa/salvar'

    $.ajax({
        type:"POST",
        url:path,
        data: {
            'areas':dados,
        },
        success: function(response){
            console.log(response)
            alert("Áreas salvas com sucesso")
        },
        error: function(xhr, ajaxOptions, thrownError){
            alert(xhr.status)
            alert(thrownError)
        },

    })

}