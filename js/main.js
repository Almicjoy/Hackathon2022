
let getStatus = function(status) {
    if (status === 0) {
        return "waiting";
    } else if (status === 1) {
        return "waiting";
    } else if (status === 2) {
        return "Ready";
    } else if (status === 3) {
        return "In Progress";
    } else if (status === 4) {
        return "On Hold";
    } else {
        return "Checked Out";
    }
}


let addRow = function() {

    var table = document.getElementById("data");

    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);

    var cell0 = row.insertCell(0);
    cell0.innerHTML = document.getElementById("fname").value + " " + document.getElementById("lname").value;

    var cell1 = row.insertCell(1);
    cell1.innerHTML = document.getElementById("id").value;
    

    var cell2 = row.insertCell(2);
    cell2.innerHTML = d


    var cell4 = row.insertCell(4);
    cell4.innerHTML = rowCount + 1

    var cell5 = row.insertCell(5);
    var element5 = document.createElement("input");
    element5.type = "checkbox";
    element5.name="chkbox[]";
    cell5.appendChild(element5);
    PatientQueue.createPatient


}

function deleteRow() {
    try {
        var table = document.getElementById("data");
        var rowCount = table.rows.length;

        for(var i=0; i<rowCount; i++) {
            var row = table.rows[i];
            var chkbox = row.cells[3].childNodes[0];
            if (null != chkbox && true === chkbox.checked) {
                table.deleteRow(i);
                rowCount--;
                i--;
            }


        for (var i=1; i < rowCount; i++) {
            var row = table.rows[i];
            row.cells[2].innerHTML = i;
        }
    }catch(e) {
        alert(e);
    }
}

