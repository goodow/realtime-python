# realtime-python

# Developing on macOS

Take the following steps to setup development with Virtualenv:

  1. Start a terminal (a shell). You'll perform all subsequent steps
     in this shell.
     
  2. Clone the repo:

     <pre>$ <b>git clone https://github.com/goodow/realtime-python.git</b>
     $ <b>cd realtime-python/</b> </pre>

  3. Install pip and Virtualenv by issuing the following commands:

     <pre>$ <b>sudo easy_install pip</b>
     $ <b>pip install --upgrade virtualenv</b> </pre>

  4. Create a Virtualenv environment:

     <pre>$ <b>virtualenv --system-site-packages -p python3 . </b> # require Python 3.n
     </pre>

  5. Activate the Virtualenv environment:

     <pre>$ <b>source ./bin/activate</b> </pre>

     The preceding `source` command should change your prompt to the following:

     <pre> (realtime-python)$ </pre>

  6. Ensure pip ≥8.1 is installed:

     <pre> (realtime-python)$ <b>easy_install -U pip</b></pre>

  7. Install all the required packages into the active Virtualenv environment:

     <pre> (realtime-python)$ <b>pip3 install --upgrade -r requirements.txt</b>


