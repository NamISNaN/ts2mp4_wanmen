const fs = require('fs') //引入node内置的文件系统
var readLine = require("readline");
var path = './test'
 
function rename() {
 var array = fs.readFileSync('name.txt').toString().split("\n");
 fs.readdir('./test/output', (err, files) => { //读取file文件夹下的文件的名字，oldName是一个数组
  var files = files.sort(function(a,b){return a-b})
  for(let i = 599 ;i<files.length;i++) {
    let oldPath =`./test/output/${files[i]}`
    let newPath =`./test/output/${array[i]}`
    fs.rename(oldPath,newPath,(err) => {
      if(err) console.log(err)
      console.log('done')
    })
  }
 if (err) {
  console.log(err)
 }


/*  for (let i = 0; i < oldName.length; i++) {
  let name = `new${i}.jpg` // 以图片为例
  newName[i] = name  // 把名字赋给一个新的数组
 }
 for (var i = 0; i < oldName.length; i++) {
  let oldPath = `./file/${oldName[i]}` //原本的路径
  let newPath = `./file/${newName[i]}` //新路径
  fs.rename(oldPath, newPath, (err) => { //重命名
  if (err) {
   console.log(err)
  }
  console.log('done!')
  })
 }
 }) */
})
}
rename()