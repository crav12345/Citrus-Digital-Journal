<div>
       <p float='left'>
              <img
                     align="left"
                     width="43"
                     src="https://piskel-imgstore-b.appspot.com/img/5a964dd1-c0e5-11ec-9d78-d53fcae61d83.gif"
                     alt="Citrus Logo"
              />
       <h1>Citrus Digital Journal</h1>
       </p>
</div>

A desktop application written in Python which functions as a private journal. Entries are encrypted and decrypted using the Advanced Encryption Standard algorithm. The application was developed solely by Christopher Ravosa as a final project for MSCS 630L Security Algorithms and Protocols at Marist College.

<sub>\* Logo by Christopher Ravosa :cowboy_hat_face:</sub>

## Advanced Encryption Standard (AES)
<p>[AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) is a specification for the encryption of electronic data established by the U.S. National Institute of Standards and Technology (NIST) in 2001. This application utilizes AES to encrypt data in groupings of 128 bits, requiring 10 rounds of encryption for every group of 16 characters. Citrus Digital Journal's AES implementation can be seen in the [aes_cipher.py](https://github.com/crav12345/Citrus-Digital-Journal/blob/main/citrus-digital-journal/aes_cipher.py) file.</p>

## Development Tools
<ul>
  <li>[Python](https://www.python.org/) programming language</li>
  <li>[Dear PyGui](https://dearpygui.readthedocs.io/en/latest/index.html#) Python GUI toolkit</li>
  <li>[SQLite](https://www.sqlite.org/index.html) self-contained database engine</li>
</ul>
