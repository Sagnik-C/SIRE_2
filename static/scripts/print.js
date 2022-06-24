
function printDiv() {
    var divContents = document.getElementById("section-to-print").innerHTML;
    var a = window.open('', '', 'height=500, width=800');
    a.document.write('<html>');
    a.document.write('<body > <h1>SIRE 2.0 Questions & Potential Grounds for Negative Observation in Page</h1> <br>');
    a.document.write(divContents);
    a.document.write('</body></html>');
    a.document.close();
    a.print();
}