*** Please read before using the program***

The motivation behind this project started when I took a course that heavily talked about steganography in school, since then I also thought it was pretty interesting.  That is why I created this simple application to hide text within pictures.

The program utilizes the stegano library which is an open source library done within python.  It was developed using the Pycharm IDE.

Capabilities: reads in a picture file that is located in the same folder as the application, it then hides whatever you want to type into the picture for safe keeping.
When you click finish it creates a new file default name is Secret_Picture.png with the added text hidden.  The program has the ability to also reveal the hidden words from the file using the reverse process.

Limitations: Currently cannot encrypt the data before hiding it, limited file types are supported (bmp,png)

What was learned doing this project?  This was my first attempt at using GUI's so I had alot of trial and error.  The stegano library was very easy to use and understand it is also still being modified. The stegano module operates by changing the least significant bits in an image in order to preserve the image as well as possible.

Steps on how to use it.

1. input picture file name into the first entry box include either the .png or .bmp
2. select if you are hiding or revealing a message
3. if hiding your message, type it into the second entry box
4. click finish
5. Your new file has just been created in the same folder 

to reveal the message repeat the same steps but select reveal, and then click finish.

