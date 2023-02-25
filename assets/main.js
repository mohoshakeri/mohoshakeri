buttons = document.getElementsByClassName('link-button')

for (let i = 0; i < buttons.length; i++) {
    const button = buttons[i];
    button.onclick = function(){

        link = button.getAttribute('link')
        target = button.getAttribute('target')
        download = button.getAttribute('download')

        let a = document.createElement('a');
        a.target = '_' + target;
        a.href = link;
        if (download != null){
            a.download = download
        }
        a.click();
    }
}