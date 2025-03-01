# LLM Model Server Project Test

<p>
    <video src="https://drive.google.com/file/d/1ZV21UANRVx0Cg6oylOvipsNmhvzSznU9/view?usp=sharing" controls> </video>
</p>

<p>
To install this LLAMA model you must install the following 

<ol>
<li> Ollama for Linux, Window or Mac </li>
<li> Nodejs </li>
<li> Python flask </li>
<li> node-fetch </li>
<li> express </li>
</ol>
</p>

## Installation 
<p> Clone the repo into your working system 

```sh
    $ git clone https://github.com/cboychinedu/virokeLlmProject.git
```

</p>


<p>
Download and install Ollama for your distribution, for this particular project, i will be using linux distro. 

<ol>

<li> Download and install Ollama </li>
Run the following command in your terminal to install Ollama: 

```sh
    $ curl -fsSL https://ollama.com/install.sh | sh

```

This script will automatically install the latest version of Ollama. 


<li> Veriffy the installation </li>
After installation, check if Ollama is installed correctly by running: 

```sh
    $ ollama --version 
```

<li> Downloading an LLMmodel in Ollama (llama) </li>
To download and install a model e.g "llama3.2:1b" run the following: 

```sh
    $ ollama pull llama3.2:1b
```

<li> Testing the downloaded model on the terminal (llama) </li>
To start interacting with the model in the terminal, use the following: 

```sh
    $ ollama run llama3.2:1b 
```


<li> Install required Python Packages/Modules inside your "PythonLLmServer" </li>
Navigate into the "PythonLLmServer" on your terminal and type the following commands 

```sh
 $ cd PythonLLmServer 
 $ pip install -r requirements.txt 

```

Affter installation, type the following commands to navigate outside the folder into your root directory 

```sh 
$  $ cd ..
```

<li> Then the next step is to navigate into your "NodejsServer" directory to install the necessary modules </li>

```sh 
    $ cd NodejsServer 
    $ npm install . 
    $ cd .. 
```
</ol>
</p>


### Start The LLM(llama) Server 

<p>
To start the llm server, type the following in the root directory: 

<ol>
<li> Make the script Executable </li> 

```sh 
    $ chmod u+x startLlmServer.sh
```

<li> Start the server </li> 

```sh
    $ bash startLlmServer.sh start 
```

<li> Check the status of the server </li> 

```sh 
    $ bash startLlmServer status 
```

<li> Stop the server </li> 

```sh 
    $ bash startLlmServer.sh stop 
```


</ol>
</p>