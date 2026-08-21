const PDFMerger = require('pdf-merger-js')
let merger = new PDFMerger();
const mergerPdfs = async(pdf1,pdf2)=>{
    await merger.add(pdf1);
    await merger.add(pdf2);
    let d = new Date().getTime()
    await merger.save(`public/${d}.pdf`);
    return d
}
module.exports = {mergerPdfs}