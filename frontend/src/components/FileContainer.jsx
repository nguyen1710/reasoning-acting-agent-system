import React from 'react'
import { FileCode } from 'lucide-react';

const FileContainer = ({fileName}) => {
    const handleDownload = () => {
    // tải file về
    const link = document.createElement("a");
    // link.href = link.fileURL
    link.download = fileName; // đặt tên file khi tải về
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };
  return (
    <div className="border rounded-lg h-fit border-primary bg-purple-100 hover:bg-purple-200 cursor-pointer" onClick={handleDownload}>
        <div className="flex items-center p-3">
            <div className="flex items-center justify-center w-12 h-12 mr-3 bg-primary rounded-lg">
                <FileCode className='text-white'/>

            </div>
            <div className="flex flex-col">
                <span className='font-semibold'>{fileName}</span>
                <span>XML</span>
            </div>
        </div>
    </div>
  )
}

export default FileContainer