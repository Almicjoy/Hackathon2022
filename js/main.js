let addRow = function() {

    var table = document.getElementById("data");

    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);

    var cell0 = row.insertCell(0);
    cell0.innerHTML = document.getElementById("fname").value + " " + document.getElementById("lname").value;

    var cell1 = row.insertCell(1);
    cell1.innerHTML = document.getElementById("id").value;

    var cell2 = row.insertCell(2);
    cell2.innerHTML = rowCount

    var cell3 = row.insertCell(3);
    var element3 = document.createElement("input");
    element3.type = "checkbox";
    element3.name="chkbox[]";
    cell3.appendChild(element3);


}

let deleteRow = function() {
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
        }

        for (var i=0; i < rowCount; i++) {
            var row = table.rows[i];
            row.cells[2].innerHTML = i + 1;
        }
    }catch(e) {
        alert(e);
    }

    return false;
}