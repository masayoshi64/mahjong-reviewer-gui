function startAnalysis() {
    file_name_element = document.getElementById("filename");
    var selected_id = file_name_element.selectedIndex;
    var file_name = file_name_element.options[selected_id].text;
    eel.analyze(file_name);
}

// setting.jsonで指定されたパスにあるjsonファイルを候補としてselect要素に追加
async function setSelect() {
    let file_names = await eel.get_file_names()();
    file_name_element = document.getElementById("filename")
    file_names.forEach(file_name => {
        const option = document.createElement('option');
        option.value = file_name;
        option.textContent = file_name;
        file_name_element.appendChild(option);
    });
}

setSelect();
