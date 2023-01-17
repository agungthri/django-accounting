

const containerDebit = document.getElementById('debit');
function delInputDebit(){
    if (containerDebit.childElementCount > 1){
        containerDebit.removeChild(containerDebit.lastChild)
        findTotalDebit()
    };
}


const containerCredit = document.getElementById('credit');
function delInputCredit(){
    if (containerCredit.childElementCount > 1){
        containerCredit.removeChild(containerCredit.lastChild)
        findTotalCredit()
    };
}



$(document).on("change", ".sum-debit", function() {
    var sum = 0;
    $(".sum-debit").each(function(){
        sum += +$(this).val();
    });
    $("#total-account-debit").val(sum.toLocaleString("id-ID", {style:"currency", currency:"IDR"}));
});



$(document).on("change", ".sum-credit", function() {
    var sum = 0;
    $(".sum-credit").each(function(){
        sum += +$(this).val();
    });
    $("#total-account-credit").val(sum.toLocaleString("id-ID", {style:"currency", currency:"IDR"}));
});



$(document).ready(function () {
    $("#debit select").chosen({
        placeholder_text_single:"Debit",
        allow_single_deselect: true});
 });
 


$(document).ready(function () {
     $("#credit select").chosen({
        placeholder_text_single:"Credit",
        allow_single_deselect: true});
  });

 

$(document).ready(function () {
    $("select").chosen({
       placeholder_text_single:"Account",
       allow_single_deselect: true});
 });



$(document).ready(function () {
    $("#add-input-debit").click(function(){
        $("#debit-account select").chosen('destroy');
        var clone = $("#debit-account").clone(true, true).find(':input[type="number"]').val("").end();
        $("#debit").append(clone)
        $("#debit-account select").chosen({
            placeholder_text_single:"Debit",
            allow_single_deselect: true});
    });
});



$(document).ready(function () {
    $("#add-input-credit").click(function(){
        $("#credit-account select").chosen('destroy');
        var clone = $("#credit-account").clone(true, true).find(':input[type="number"]').val("").end();
        $("#credit").append(clone)
        $("#credit-account select").chosen({
            placeholder_text_single:"Credit",
            allow_single_deselect: true});
    });
});

