function startAnalysis() {
    var file_name_element = document.getElementById("filename")
    var kyoku_name_element = document.getElementById("kyokuname")
    var selected_id = file_name_element.selectedIndex;
    var file_name = file_name_element.options[selected_id].text;
    var kyoku_name_selected_id = kyoku_name_element.selectedIndex;
    eel.analyze(file_name, kyoku_name_selected_id);
}

// setting.jsonで指定されたパスにあるjsonファイルを候補としてselect要素に追加
async function setFileName() {
    var file_names = await eel.get_file_names()();
    var file_name_element = document.getElementById("filename")
    file_names.forEach(file_name => {
        const option = document.createElement('option');
        option.value = file_name;
        option.textContent = file_name;
        file_name_element.appendChild(option);
    });
    updateKyokuName();
}

async function updateKyokuName() {
    var file_name_element = document.getElementById("filename")
    var kyoku_name_element = document.getElementById("kyokuname")
    var selected_id = file_name_element.selectedIndex;
    var file_name = file_name_element.options[selected_id].text;
    var kyoku_names = await eel.get_kyoku_names(file_name)()
    kyoku_names.forEach(kyoku_name => {
        const option = document.createElement('option');
        option.value = kyoku_name;
        option.textContent = kyoku_name;
        kyoku_name_element.appendChild(option);
    });
}

setFileName();
