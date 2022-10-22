

var statuses = ["Waiting", "Ready", "In Progress", "On Hold", "Checked Out"]
var rooms = []

for (var i = 0; i < 3; i++) {
    rooms[i] = true
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
    var dropdown = document.createElement("select");

    for(var i = 0; i < statuses.length; i++) {
        var opt = document.createElement("option")
        opt.text = statuses[i]
        dropdown.add(opt)
    }
    cell2.appendChild(dropdown)

    var cell4 = row.insertCell(3);
    var found_room = false
    for (var x = 0; x < rooms.length; x++) {
        if (rooms[x]) {
            found_room = true
            rooms[x] = false
            cell4.innerHTML = "Room " + (x + 1);
            break;
        }
    }


    var cell3 = row.insertCell(4);
    var element3 = document.createElement("input");
    element3.type = "checkbox";
    element3.name="chkbox[]";
    cell3.appendChild(element3);
    PatientQueue.createPatient


}

let deleteRow = function() {
    try {
        var table = document.getElementById("data");
        var rowCount = table.rows.length;

        for(var i=0; i<rowCount; i++) {
            var row = table.rows[i];
            var chkbox = row.cells[4].childNodes[0];
            if (null != chkbox && true === chkbox.checked) {
                table.deleteRow(i);
                rowCount--;
                i--;
            }
        }

    }catch(e) {
        alert(e);
    }

    return false;
}

