import "PatientQueue"

let addRow = function() {

    var table = document.getElementById("data");

    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);

    var cell0 = row.insertCell(0);
    cell0.innerHTML = document.getElementById("fname").value + " " + document.getElementById("lname").value;

    var cell1 = row.insertCell(1);
    cell1.innerHTML = document.getElementById("id").value;
    

    var cell2 = row.insertCell(2);
    var element2 = document.createElement("input");
    element2.type = "text";
    element2.name = "txtbox[]";
    cell3.appendChild(element2);

    var cell3 = row.insertCell(3);
    var element3 = document.createElement("input");
    element3.type = "checkbox";
    element3.name="chkbox[]";
    cell3.appendChild(element3);
    PatientQueue.createPatient


}

function deleteRow() {
    try {
        var table = document.getElementById("data");
        var rowCount = table.rows.length;

        for(var i=0; i<rowCount; i++) {
            var row = table.rows[i];
            var chkbox = row.cells[0].childNodes[0];
            if(null != chkbox && true == chkbox.checked) {
                table.deleteRow(i);
                rowCount--;
                i--;
            }


        }
    }catch(e) {
        alert(e);
    }
}