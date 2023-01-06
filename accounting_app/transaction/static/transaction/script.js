

const containerDebit = document.getElementById('debit');
function addInputDebit(){
    const node = document.getElementById("debit-hidden");
    const clone = node.cloneNode(true);
    clone.hidden = false;
    containerDebit.appendChild(clone);
}


function delInputDebit(){
    if (containerDebit.childElementCount > 1){
        containerDebit.removeChild(containerDebit.lastChild)
        findTotalDebit()
    };
}


const containerCredit = document.getElementById('credit');
function addInputCredit(){
    const node = document.getElementById("credit-hidden");
    const clone = node.cloneNode(true);
    clone.hidden = false;
    containerCredit.appendChild(clone);
}
  

function delInputCredit(){
    if (containerCredit.childElementCount > 1){
        containerCredit.removeChild(containerCredit.lastChild)
        findTotalCredit()
    };
}


function findTotalDebit(){
    var arr = document.getElementsByClassName("sum-debit");
    var total = 0;
    for( var i = 0; i < arr.length; i++ ){
        if( parseInt(arr[i].value) )
            total += parseInt(arr[i].value);
    }
    document.getElementById('total-account-debit').value = total;
}


function findTotalCredit(){
    var arr = document.getElementsByClassName("sum-credit");
    var total = 0;
    for( var i=0; i<arr.length; i++){
        if( parseInt(arr[i].value))
            total += parseInt(arr[i].value);
    }
    document.getElementById('total-account-credit').value = total;
}