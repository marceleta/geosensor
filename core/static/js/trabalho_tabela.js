var url = $('#form').data('urlajax')

$(document).ready(function(){
    let hoje = new Date()

    let mes = Number(hoje.getMonth()) + Number(1)

    dia = hoje.getDate()

    if(dia <= 9){
        dia = '0'+ dia
    }

    let data = hoje.getFullYear() +"-0"+mes+"-"+dia

    $('#data').val(data)
    setDisableHoraFinal(true)
})




$('#pesquisa').click(function(){

    let data = $('#data').val()
    let hinicio = $('#hinicio').val()
    let hfinal = $('#hfinal').val()
    let trator = $('#trator').val()

    $.ajax({
        url:url,
        data:{
            'data':data, 
            'hinicio':hinicio, 
            'hfinal':hfinal, 
            'trator':trator
        },
        success: function(response){
            $('#trabalhos').html(response)
            
        }
    })


})

$('#hinicio').keyup(function(){
    let h_inicio = $('#hinicio').val()

    if (h_inicio != ""){
        console.log(h_inicio)
        setDisableHoraFinal(false)
    }
    
})

$('#limpar').click(function(){
    console.log('limpar')
    $.ajax({
        url:url,
        data:{
            'data':'', 
            'hinicio':'', 
            'hfinal':'', 
            'trator':0
        },
        success: function(response){
            console.log(response)
            $('#trabalhos').html(response)
            
        }
    })

})

function setDisableHoraFinal(boleano){
    $('#hfinal').prop('disabled', boleano)
}