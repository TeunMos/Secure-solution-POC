const host = 'http://localhost:3000';
const socket = io(host);


let luggageList = [];
let gateList = [];

window.onload = () => {
    
}

socket.on('connect', () => {
    console.log('connected');
    socket.emit('getLuggage');
});

socket.on('disconnect', () => {
    console.log('disconnected');
});



socket.on('luggageAdded', (data) => {
    addLuggage(data);
});

socket.on('luggageUpdated', (data) => {
    updateLuggage(data);
});

socket.on('luggageDeleted', (data) => {
    deleteLuggage(data);
});



socket.on('allLuggage', (data) => {
    luggageList = data;
    console.log(luggageList);
    updateLuggageTable();
});

socket.on('allGates', (data) => {
    console.log(data);
    
});

function fillTable(tableId, data) {
    const table = document.getElementById(tableId);
    table.innerHTML = '';

    // Create table header
    const header = table.createTHead();
    const headerRow = header.insertRow();

    Object.keys(data[0]).forEach(key => {
        headerRow.insertCell().innerHTML = key;
    });

    // Create table body
    const body = table.createTBody();
    data.forEach(d => {
        const row = body.insertRow();
        Object.keys(d).forEach(key => {
            row.insertCell().innerHTML = d[key];
        });
    }
    );

}

function updateLuggageTable() {

    let _luggageList = [];
    luggageList.forEach(l => {
        _luggageList.push({
            tag: l.id,
            location: l.location,
        });
    });
    
    fillTable('luggageTable', _luggageList)

    const checkinList = _luggageList.forEach(l => { l.location.startsWith('checkin') });
    if (checkinList.length > 0) {
        fillTable('checkedInTable', checkinList);
    }
    
    const storageTable = _luggageList.forEach(l => { l.location.startsWith('storage') });
    if (securityList.length > 0) {
        fillTable('securityTable', securityList);
    }
    fillTable('storageTable', _luggageList.forEach(l => { l.location.startsWith('storage') }));

    readyTable('readyTable', gateList.forEach(l => { l.location.startsWith('gate') }));
}





function addLuggage(luggage) {
    luggageList.push(luggage);

    const row = luggageTable.insertRow();
    row.id = luggage.id;
    
}

function updateLuggage(luggage) {
    luggageList.forEach(l => {
        luggageList.forEach((l, index) => {
            if (l.id === luggage.id) {
                luggageList[index] = luggage;
            }
        });
    });
}

function deleteLuggage(luggage) {
    luggageList.forEach((l, index) => {
        if (l.id === luggage.id) {
            luggageList.splice(index, 1);
        }
    });
}