const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow

let url
if (process.env.NODE_ENV === 'DEV') {
    url = 'http://localhost:9000/'
} else {
    url = `file://${process.cwd()}/dist/index.html`
}

app.on('ready', () => {
    let window = new BrowserWindow({ width: 800, height: 600 });
    window.loadURL(url);
    window.webContents.openDevTools();
    window.on('closed', () => {
        // 取消引用 window 对象，如果你的应用支持多窗口的话，
        // 通常会把多个 window 对象存放在一个数组里面，
        // 与此同时，你应该删除相应的元素。
        win = null
    })
})
