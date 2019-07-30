const electron = require('electron')
const app = electron.app
const { BrowserWindow, Menu } = electron

let url
if (process.env.NODE_ENV === 'DEV') {
    url = 'http://localhost:9000/'
} else {
    url = 'http://47.101.218.207:8080'
}

const toolbarTemplate = [
    {
        label: 'File',
        submenu: [
            {
                role: 'close'
            }
        ]
    },
    {
        label: 'Edit',
        submenu: [
            {role: 'undo'},
            {role: 'redo'},
            {type: 'separator'},
            {role: 'cut'},
            {role: 'copy'},
            {role: 'paste'},
            {role: 'delete'},
            {type: 'separator'},
            {role: 'selectall'}
        ]
    },
    {
        label: 'View',
        submenu: [
            {type: 'separator'},
            {role: 'resetzoom'},
            {role: 'zoomin'},
            {role: 'zoomout'}
        ]
    },
    {
        role: 'window',
        submenu: [
            {role: 'minimize'},
            {role: 'close'}
        ]
    }
]
const title = require("./package.json").name;
  

app.on('ready', () => {
    let window = new BrowserWindow({ width: 800, height: 600, title: title });
    window.loadURL(url);
    const menu = Menu.buildFromTemplate(toolbarTemplate);
    window.setTitle(title);
    window.setMenu(menu);
    // Menu.setApplicationMenu(menu)
    window.on('closed', () => {
        // 取消引用 window 对象，如果你的应用支持多窗口的话，
        // 通常会把多个 window 对象存放在一个数组里面，
        // 与此同时，你应该删除相应的元素。
        win = null
    })
})
