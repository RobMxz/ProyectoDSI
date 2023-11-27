var popUp;

function mostrarNotificacion() {
    let i=0;
    if(i==1){
        popUp = document.getElementById("exitoso"); 
        popUp.showModal();  
    }
    else{
        popUp = document.getElementById("fallido"); 
        popUp.showModal(); 
    }    
}


function cerrarNotificacion() {  
    popUp.close(); 
}
