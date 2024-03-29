# Table of contents
0. [Installation](#installation)
1. [Introduction](#Introduction)
    1. [Purpose](#purpose)
    2. [Requirements](#requirements)
        1. [Step 1](#step-1)
        2. [Step 2](#step-2)
        3. [Step 3](#step-3)
        4. [Step 4](#step-4)
    3. [Footnotes](#footnotes)
    4. [Recognizers](#recognizers)
        * [Dollar Family Recognizers](#dollar-family)
            * [$1](#one-dollar)
            * [$Q](#q-dollar)
            * [Penny Pincher](#q-dollar)
    5. [Implementation](#implementation)
    6. [Deliverables](#deliverables)
    7. [Grading and Notes](#grading-and-notes)    
2. [Successes and Resources](#successes-and-resources)
   * [GitHub](#github)
   * [Jet Brains](#jet-brains)
   * [Markdown Reference](#markdown)
   * [Tkinter](#tkinter)
   * [Numpy](#numpy)
   * [Matplotlib](#matplotlib)
3. [Problems Encountered](#problems-encountered)
   * [Qt](#qt)
   * [PyInstaller](#pyinstaller)
4. [Bugs](#bugs)
    * [Recognizers](#recog_bug)
    * [Comparisons](#comparisons)
5. [Improvement](#improvements)
   * [Numpy Operations](#imp_numpy)

# <a id="installation"/>
<h3>After installing and extracting the .ZIP from GitHub do the following:</h3>
<h4> Install <a href="https://www.python.org/downloads/">Python</a> if you haven't!</h4>
<h4>python -m pip install --upgrade pip<br></h4>
<h4>pip install numpy<br></h4>
<h4>pip install tkinter<br></h4>
<h4>python main.py</h4>
Select the 'Pre-Trained' option

<h1>Project 1 – Exploring $-family recognizers</h1>
<h5><a href="https://canvas.unf.edu/courses/100860/assignments/1328145.com]">Submission</a> Due: 2/8/24 11:59 pm<h5/> 


This project was created by John S. Reddick. The outline of the following project requirements are adapted from the 
    project description created by Corey Pittman in 2024. I have included an original copy of the instructions as written by Dr. Pittman 
    <a href="https://github.com/John-S-Reddick/resume-reference/blob/main/CIS4930%20Novel%20User%20Interfaces/Project%201/SpecialTopicsProj1.pdf" >here</a>

<ol>
 <a id="purpose"/> <h2><li> Purpose</h2>
            The purpose of this assignment is twofold.
             <ol>
                 <li> -[X] Gain experience with simple recognizers using reliable data (touch/stylus/mouse).</li>
                 <li> -[X] Gain experience with implementing a state-of-the-art algorithms from scratch by relying on algorithms provided in
                    the research paper</li>
            </ol>

 <a id="requirements"/> <h2><li> Requirements</h2>
     <ol>
    <a id="step-1"/><h3><li>Step 1 create some kind of basic canvas drawing application ^1</h3>
    <ol>
        <li>-[X] Create a window</li>
        <li>-[X] Create a canvas on which to draw</li>
        <ol>
            <li>-[X] Track mouse click</li>
            <li>-[X] Track mouse movements</li>
            <li>-[X] Paint mouse movements on drawing canvas</li>
            <li>-[X] Increase Stoke count on mouse click</li>
            <li>-[X] Save raw X, Y Coordinates and stroke count to list as numpy array</li>
        </ol>
        <li> Create a canvas that displays what the recognizer sees</li>
        <li>-[X] On the bottom display which template is most likely visually</li>
    </ol>
     <h4>Create buttons or widgets to do the following:</h4>
    <ol>
        <li>-[X] Create a submit button and function to write coordinates to file</li>
        <li>-[X] Undo previous written strokes</li>
        <li>-[X] Clear the canvas</li>
        <li>-[X] Trigger recognition</li>
    </ol>
    </li>
    <a id="step-2"/><h3><li>Step 2 Implement Dollar Family Recognizers</h3>    
    <ol>
        <li>-[X] $1</li>
        <li>-[ ] $Q</li>
        <li>-[X] Penny Pincher</li>
    </ol>
    </li>
    <a id="step-3"/><h3><li>Step 3 Training</h3> Test each recognizer by writing each symbol 5 times, which should give you a good accuracy number
    <ol>
        <li>-[X] Train each recognizer with the following symbols: 0,1,2,3,4,5,6,7,8,9,+,-,*,t,a,n,s,c,i</li>
        <li>-[X] Include the square root symbol and some more oddball symbols of your own choosing</li>
        <li>-[X] Train each recognizer with 1, 3, and 5 samples per symbol</li>
    </ol>
    </li>
    <a id="step-4"/><h3><li>Step 4 Documentation and Comparison</h3> Test each recognizer by writing each symbol 5 times, which should give you a good accuracy number
     <ol>
         <li>-[ ] Document results of your experiment in your README file</li>
         <li>-[ ] Compare each of them.</li>
         <li>-[ ] Run separate experiments using the data you collected using a mouse vs a touch screen (if applicable)</li>
     </ol>
     </li>
     </ol>   
<a id="footnotes"/><h2><li>Footnotes</h2>
    <ol>
        <li>            
            This can be done in any programming language of your choosing, though Dr. Pittman recommends looking into
            capabilities of C# with WPF, Python with TK, Java with Swing, or HTML/JS/CSS. No choice is
            inherently better than others.
        <li>
            Dr. Pittman reccomends
            https://www.eecs.ucf.edu/isuelab/demo/stochastic-resampling/ or
            https://depts.washington.edu/acelab/proj/dollar/index.html for examples of similar canvas
            implementations, Dr. Pittman offered to reccomend additional examples as needed.
        </li>            
    </ol>
<a id="recognizers"/> <h2><li> Recognizers</h2>
            <a id="dollar-family"/> <h3>$ Family Recognizer Round-Up <a  href="https://depts.washington.edu/acelab/proj/dollar/index.html">Link</a></h3>
            <ol>
                <a id="one-dollar"/> <h4><li>$1 Recognizer <a  href="http://faculty.washington.edu/wobbrock/pubs/uist-07.01.pdf">Link</a></h4>
                <a  href="https://dl.acm.org/doi/10.1145/1294211.1294238">DOI</a> Wobbrock, J.O., Wilson, A.D. and Li, Y. (2007).<br>
                Gestures without libraries, toolkits or training: A $1 recognizer for user interface prototypes. <br>
                Proceedings of the ACM Symposium on User Interface Software and Technology (UIST '07). Newport, Rhode Island (October 7-10, 2007).<br>
                New York: ACM Press, pp. 159-168.<br>
                </li>
                <a id="q-dollar"/> <h4><li>$Q Recognizer <a href="http://faculty.washington.edu/wobbrock/pubs/mobilehci-18.pdf">Link</a></h4>
                <a  href="https://dl.acm.org/doi/10.1145/3229434.3229465">DOI</a> Vatavu, R.-D., Anthony, L. and Wobbrock, J.O. (2018).<br>
                $Q: A super-quick, articulation-invariant stroke-gesture recognizer for low-resource devices.<br>
                Proceedings of the ACM Conference on Human-Computer Interaction with Mobile Devices and Services (MobileHCI '18).<br>
                Barcelona, Spain (September 3-6, 2018). New York: ACM Press. Article No. 23.<br>
                </li>
                <a id="penny-pincher"/><h4><li>Penny Pincher Recognizer <a href="https://www.eecs.ucf.edu/isuelab/publications/pubs/gi2015_eugene.pdf">Link</a></h4>
                <a  href="https://dl.acm.org/doi/10.5555/2788890.2788925">DOI</a> Eugene M. Taranta, II and Joseph J. LaViola, Jr. (2015). <br>
                Penny Pincher: A Blazing Fast, Highly Accurate $-family Recognizer. <br>
                In Proc. of GI ’15. 195–202 <br>
                </li>     
            </ol>
<a id="implementation"/><h2><li> Implementation</h2>
            To  your symbol recognizers, there are some things you need to consider.
            1. You need to find a way to invoke the recognizer. You can have it run in real time or in
            batch mode (by pressing a button or doing a different, heuristically determined gesture)            
            2. You will need to show recognition results to the user. A simple text box is fine but if you
            want to be more elaborate feel free to do so.

<a id="deliverables"/><h2><li> Deliverables</h2>
    <ol>
        <li>-[X] Upload your source code to Canvas <a href="https://canvas.unf.edu/courses/100860/assignments/1328145.com]">here</a></li>
        <li>-[X] Include a README</li>
    </ol>
    <h2>In the README:</h2>
    <ol>
        <li>-[X] Cite papers in recognizers section</li>
        <li>-[X] Describe what works</li>
        <li>-[X] Describe what doesn't work</li>
        <li>-[ ] Results of your experiments</li>
        <li>-[X] Any known bugs</li>
        <li>-[X] Problems you encountered</li>
        <li>-[X] Bonus: Room for Improvement</li>
    </ol>

<a id="grading-and-notes"/><h2><li> Grading and Notes</h2>
            80% correct implementation of the recognizers
            20% documentation

</ol>
<a id="successes-and-resources"/>
<h1>Successes and Resources</h1>
<ol>
    <a id="github"/><h2><li> GitHub</h2>
        This project has been an excellent way to learn and teach myself how to use GitHub. GitHub is an industry standard, and the oppurtunity to become familiar with it is invaluable.
        The convenience of GitHub will allow me to revert any changes I have made to my code which I have taken advantage of plenty of times, and It will also allow me to change development devices with no hassle.
        Over the course of this project I will be out of town and away from my primary development workstation, but my laptop will be able to make use of the repository for seamless development.
    </li>
    <a id="jet-brains"/><h2><li> Jet Brains</h2>
        I originally used <a href="https://www.jetbrains.com/clion/download/#section=windows">CLion</a> to develop with C++, but have since switched to JetBrain's
        <a href="https://www.jetbrains.com/pycharm/download/">PyCharm</a> for development. These have been massive successes and make for easy integration with GitHub,
        allowing me to push updates to the repository through graphical mouse based interface, and through the command line.
    </li>
    <a id="markdown"/><h2><li> Markdown Reference</h2>
        The markdown reference guide <a href="https://www.markdownguide.org/basic-syntax/")>here</a> has allowed me to document my readme in style while also empowering this readme
        to act as a repository for useful links for my current and future self. To anyone who comes across this project in the future. My table of contents is from 
        <a href="https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents#27953547")>this</a> Stack exchange article.
        If you want a fancy readme, call it readme.md and follow the link! Much fancier than readme.me (or even readme.txt)
    </li>
    <a id="tkinter"/><h2><li> Tkinter</h2>
        Tkinter was much more helpful than Qt, and easier to start. I am already familiar with Tkinter, so it was a breeze to get started.
        The ability to size canvases and track mouse movements was very easy. Documentation and references to resources will be included in relevent code
    </li>
    <a id="numpy"/><h2><li> Numpy</h2>
        <a href="https://numpy.org")>"Numpy</a> 
         is the fundamental package for scientific computing in Python.
         It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on
         arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more."
        <h4>- Numpy home page</h4> 
        <br><br> Numpy allows me to do quick and in depth mathematics on my data, and make plotting it easy! I already have experience with NumPy so I hope to use it in conjunction with MatPlotLib to create my visualizations
    </li>
    <a id="matplotlib"/><h2><li>MatPlotLib</h2>
        <a href="https://matplotlib.org")>MatPlotLib</a> is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible. Create publication quality plots. Make interactive figures that can zoom, pan, update. Customize visual style and layout. Export to many file formats. Embed in JupyterLab and Graphical User Interfaces. Use a rich array of third-party packages built on Matplotlib.<br>
    - Matplotlib home page <br><br>
        I can use my existing experience with Matplotlib to create viusalizations and comparisons for <a href="#step-4")>step 4</a>
</ol>

<a id="problems-encountered"></a>
<h1>Problems encountered</h1>
<ol>
    <a id="qt"></a><h2><li> QT</h2>
            I attempted to use the Qt C++ Library, but it became too unwieldly to implement.
            I would like to implement Qt and take advantage of C++, but based on previous experience 
            with the Qt library I know I would be better suited to deveolping on Linux where Qt plays a little more nicely.
            This diversion would eat into the time necessary to finish the project so I will be abstaining from that.
            Instead I have switched over to Python and the Tkinter library.
    </li>
    <a id="pyinstaller"/><h2><li>PyInstaller</h2>
        <a href="https://pyinstaller.org/en/stable/")>PyInstaller</a> Didn't like some of my math. Things that work in python don't work when PyInstaller made it into an executable

</ol>
<a id="bugs"/>
<h1>Bugs</h1>
<ol>
    <a id="recog_bug"></a><h2><li>Recognizers</h2>
        The $1 and Penny Pincher Recognizers have suddenly stopped accurately recognizing gestures when I haven't changed anything. I'll need to look into what's causing these issues    
    </li>
    <a id="comparisons"></a><h2><li>Comparisons</h2>
        The issues with recognizers having suddenly stopped working has made it difficult to compare them    
    </li>

</ol>
<a id="improvements"/>
<h1>Improvement</h1>
<ol>
    <a id="imp_numpy"></a><h2><li>Numpy operations</h2>
        Numpy has many powerful abilities to perform efficient operations on the arrays. While the math is sufficient, I would want to use even more of esoteric NumPy operations
    </li>
</ol>

