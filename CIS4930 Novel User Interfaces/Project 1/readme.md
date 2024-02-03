# Table of contents
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
3. [Problems Encountered](#problems-encountered)
    * [Qt](#qt)

## Introduction
<h1>Project 1 – Exploring $-family recognizers</h1>
<h5><a href="https://canvas.unf.edu/courses/100860/assignments/1328145.com]">Submission</a> Due: 2/8/24 11:59 pm<h5/>  

This project was created by John S. Reddick. The outline of the following project requirements are adapted from the 
    project description created by Corey Pittman in 2024. I have included an original copy of the instructions as written by Dr. Pittman 
    <a href="https://github.com/John-S-Reddick/resume-reference/blob/main/CIS4930%20Novel%20User%20Interfaces/Project%201/SpecialTopicsProj1.pdf" >here</a>

<ol>
 <a name="purpose"/> <h2><li> Purpose</h2>
            The purpose of this assignment is twofold.
             <ol>
                 <li> -[ ] Gain experience with simple recognizers using reliable data (touch/stylus/mouse).</li>
                 <li> -[ ] Gain experience with implementing a state-of-the-art algorithms from scratch by relying on algorithms provided in
                    the research paper</li>
            </ol>

 <a name="requirements"/> <h2><li> Requirements</h2>
     <ol>
    <a name="step-1"/><h3><li>Step 1 create some kind of basic canvas drawing application ^1</h3>
    <ol>
        <li>-[X] Create a window</li>
        <li>-[ ] Create a canvas on which to draw, and a canvas that displays what the recognizer sees</li>
        <li>-[ ] Track mouse movements</li>
        <li>-[ ] On the bottom display which template is most likely visually</li>
        <li>-[ ] Save raw X, Y Coordinates and stroke count as data points in CSV files</li>
    </ol>
     <h4>Create buttons or widgets to do the following:</h4>
    <ol>
        <li>-[ ] Clear the canvas</li>
        <li>-[ ] Tell the application when to save</li>
        <li>-[ ] Trigger recognition</li>
        <li>-[ ] Undo previous written strokes</li>
    </ol>
    </li>
    <a name="step-2"/><h3><li>Step 2 Implement Dollar Family Recognizers</h3>    
    <ol>
        <li>-[ ] $1</li>
        <li>-[ ] $Q</li>
        <li>-[ ] Penny Pincher</li>
    </ol>
    </li>
    <a name="step-3"/><h3><li>Step 3 Training</h3> Test each recognizer by writing each symbol 5 times, which should give you a good accuracy number
    <ol>
        <li>-[ ] Train each recognizer with with the following symbols: 0,1,2,3,4,5,6,7,8,9,+,-,*,t,a,n,s,c,i</li>
        <li>-[ ] Include the square root symbol and some more oddball symbols of your own choosing</li>
        <li>-[ ] Train each recognizer with 1, 3, and 5 samples per symbol</li>
    </ol>
    </li>
    <a name="step-4"/><h3><li>Step 4 Documentation and Comparison</h3> Test each recognizer by writing each symbol 5 times, which should give you a good accuracy number
     <ol>
         <li>-[ ] Document results of your experiment in your README file</li>
         <li>-[ ] Compare each of them.</li>
         <li>-[ ] Run separate experiments using the data you collected using a mouse vs a touch screen (if applicable)</li>
     </ol>
     </li>
     </ol>   
<a name="footnotes"/><h2><li>Footnotes</h2>
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
<a name="recognizers"/> <h2><li> Recognizers</h2>
            <a name="dollar-family"/> <h3>$ Family Recognizer Round-Up <a  href="https://depts.washington.edu/acelab/proj/dollar/index.html">Link</a></h3>
            <ol>
                <a name="one-dollar"/> <h4><li>$1 Recognizer <a  href="http://faculty.washington.edu/wobbrock/pubs/uist-07.01.pdf">Link</a></h4>
                Wobbrock, J.O., Wilson, A.D. and Li, Y. (2007).<br>
                Gestures without libraries, toolkits or training: A $1 recognizer for user interface prototypes. <br>
                Proceedings of the ACM Symposium on User Interface Software and Technology (UIST '07). Newport, Rhode Island (October 7-10, 2007).<br>
                New York: ACM Press, pp. 159-168.<br>
                <a  href="https://dl.acm.org/doi/10.1145/1294211.1294238">DOI</a>
                </li>
                <a name="q-dollar"/> <h4><li>$Q Recognizer <a href="http://faculty.washington.edu/wobbrock/pubs/mobilehci-18.pdf">Link</a></h4>
                Vatavu, R.-D., Anthony, L. and Wobbrock, J.O. (2018).<br>
                $Q: A super-quick, articulation-invariant stroke-gesture recognizer for low-resource devices.<br>
                Proceedings of the ACM Conference on Human-Computer Interaction with Mobile Devices and Services (MobileHCI '18).<br>
                Barcelona, Spain (September 3-6, 2018). New York: ACM Press. Article No. 23.<br>
                <a  href="https://dl.acm.org/doi/10.1145/3229434.3229465">DOI</a>
                </li>
                <a name="penny-pincher"/><h4><li>Penny Pincher Recognizer <a href="https://www.eecs.ucf.edu/isuelab/publications/pubs/gi2015_eugene.pdf">Link</a></h4>
                </li>     
            </ol>
<a name="implementation"/><h2><li> Implementation</h2>
            To  your symbol recognizers, there are some things you need to consider.
            1. You need to find a way to invoke the recognizer. You can have it run in real time or in
            batch mode (by pressing a button or doing a different, heuristically determined gesture)            
            2. You will need to show recognition results to the user. A simple text box is fine but if you
            want to be more elaborate feel free to do so.

<a name="deliverables"/><h2><li> Deliverables</h2>
    <ol>
        <li>-[ ] Upload your source code to Canvas <a href="https://canvas.unf.edu/courses/100860/assignments/1328145.com]">here</a></li>
        <li>-[X] Include a README</li>
    </ol>
    <h2>In the README:</h2>
    <ol>
        <li>-[ ] Cite papers in recognizers section</li>
        <li>-[ ] Describe what works</li>
        <li>-[ ] Describe what doesn't work</li>
        <li>-[ ] Results of your experiments</li>
        <li>-[ ] Any known bugs</li>
        <li>-[ ] Problems you encountered</li>
        <li>-[ ] Bonus: Room for Improvement</li>
    </ol>

<a name="grading-and-notes"/><h2><li> Grading and Notes</h2>
            80% correct implementation of the recognizers
            20% documentation

</ol>
<a name="successes-and-resources"/>
<h1>Successes and Resources</h1>
<ol>
    <a name="github"/><h2><li> GitHub</h2>
        This project has been an excellent way to learn and teach myself how to use GitHub. GitHub is an industry standard, and the oppurtunity to become familiar with it is invaluable.
        The convenience of GitHub will allow me to revert any changes I have made to my code which I have taken advantage of plenty of times, and It will also allow me to change development devices with no hassle.
        Over the course of this project I will be out of town and away from my primary development workstation, but my laptop will be able to make use of the repository for seamless development.
    </li>
    <a name="jet-brains"/><h2><li> Jet Brains</h2>
        I originally used <a href="https://www.jetbrains.com/clion/download/#section=windows">CLion</a> to develop with C++, but have since switched to JetBrain's
        <a href="https://www.jetbrains.com/pycharm/download/">PyCharm</a> for development. These have been massive successes and make for easy integration with GitHub,
        allowing me to push updates to the repository through graphical mouse based interface, and through the command line.
    </li>
    <a name="markdown"/><h2><li> Markdown Reference</h2>
        The markdown reference guide <a href="https://www.markdownguide.org/basic-syntax/")>here</a> has allowed me to document my readme in style while also empowering this readme
        to act as a repository for useful links for my current and future self. To anyone who comes across this project in the future. My table of contents is from 
        <a href="https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents#27953547")>this</a> Stack exchange article.
        If you want a fancy readme, call it readme.md and follow the link! Much fancier than readme.me (or even readme.txt)
    </li>
    <a name="tkinter"/><h2><li> Tkinter</h2>
        Tkinter was much more helpful than Qt, and easier to start. I am already familiar with Tkinter, so it was a breeze to get started.
        The ability to size canvases and track mouse movements was very easy.
    </li>
</ol>

<a name="problems-encountered"/>
<h1>Problems encountered</h1>
<ol>
    <a name="qt"/><h2><li> QT</h2>
            I attempted to use the Qt C++ Library, but it became too unwieldly to implement.
            I would like to implement Qt and take advantage of C++, but based on previous experience 
            with the Qt library I know I would be better suited to deveolping on Linux where Qt plays a little more nicely.
            This diversion would eat into the time necessary to finish the project so I will be abstaining from that.
            Instead I have switched over to Python and the Tkinter library.
    </li>
</ol>

