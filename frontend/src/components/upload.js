import React, {useState} from 'react';
import axios from 'axios';

function Upload() {

    const [title, setTitle] = useState("");
    const [file_license, setFileLicense] = useState(null);

    const onTitleChange = event => setTitle(event.target.value);
    const onLicenceFileChange = event => setFileLicense(event.target.files[0]);

    const newBook = async () => {
        const uploadData = new FormData();
        uploadData.append('title', title);
        uploadData.append('file_license', file_license);

        try {
            return await axios.post(
                'http://127.0.0.1:8000/uploads/', uploadData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            )
        } catch (e) {
            return e.response ? e.response : e
        }
    }

 return (
    <div className="App">
      <h3>Choose your parameters and file. </h3>
      <label>
        Parameters
        <input
          className="upload-field"
          type="text"
          value={title}
          onChange={onTitleChange}/>
      </label>
      <br/>
      <label>
        Select File
        <input
          className="upload-field"
          type="file"
          onChange={onLicenceFileChange} />
      </label>
      <br/>

      <button className="upload-field" onClick={() => { newBook(); start_convert();}}>Upload File</button><br/>
    </div>


  );
}

export default Upload;
