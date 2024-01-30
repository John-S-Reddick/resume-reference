<h1>Introduction</h1>
<h1>Project 1 – Exploring $-family recognizers</h1>
<h5>Due: 2/8/24 11:59 pm<h5/>  <a href="https://canvas.unf.edu/courses/100860/assignments/1328145.com]">Submission</a>

This project was created by John S. Reddick. The outline of the following project requirements are adapted from the 
    project description created by Corey Pittman in 2024. I have included an original copy of the instructions 
    <a href="https://github.com/John-S-Reddick/resume-reference/blob/main/CIS4930%20Novel%20User%20Interfaces/Project%201/SpecialTopicsProj1.pdf">here</a>

<ol>
    <li> <h2>Purpose</h2>
            The purpose of this assignment is twofold. It is first designed to give you experience with simple
            recognizers using reliable data (touch/stylus/mouse). Second, it is to give you experience with
            implementing a state-of-the-art algorithms from scratch by relying on algorithms provided in
            the research paper
    </li>    
    <li> <h2>Requirements</h2>
            There are two main requirements for this assignment. First, you will implement 3 $- family
            recognizers and compare them.        
            Train each recognizer with 1, 3, and 5 samples per symbol. Test each recognizer by writing each
            symbol 5 times, which should give you a good accuracy number. You should run separate
            experiments using the data you collected using a mouse vs a touch screen (if applicable). Please
            put the results of your experiment in your README file.
            In contrast to the directions as described in the original instructions written by Dr. Pittman and with his consent, I will
            be using the %1 recognizer, the $Q recognizer, and Penny Pincher.
    </li>
    <li> <h2>Recognizers</h2>        
            You should test these algorithms with the following symbols: 0,1,2,3,4,5,6,7,8,9,+,-,*,t,a,n,s,c,i,
            and the square root symbol. I would also recommend adding some more oddball symbols of
            your own choosing
            (Here I will provide citations to the pages)
            <a href="http://faculty.washington.edu/wobbrock/pubs/uist-07.01.pdf">$1</a>
            <b/>
            <a href="http://faculty.washington.edu/wobbrock/pubs/mobilehci-18.pdf">$Q</a>
            <b/>
            <a href="https://www.eecs.ucf.edu/isuelab/publications/pubs/gi2015_eugene.pdf">Penny Pincher</a>            
    </li>
    <li> <h2>Strategy</h2>
            The first step of this project is to create some kind of basic canvas drawing application. This can
            be done in any programming language of your choosing, though I recommend looking into the
            capabilities of C# with WPF, Python with TK, Java with Swing, or HTML/JS/CSS. No choice is
            inherently better than others. You will want to create buttons or widgets to enable the user to
            clear the canvas, trigger recognition, and undo previous written strokes. Please see
            https://www.eecs.ucf.edu/isuelab/demo/stochastic-resampling/ or
            https://depts.washington.edu/acelab/proj/dollar/index.html for examples of similar canvas
            implementations which you can work from. Reach out to the instructor if more examples are
            needed.
    </li>
    <li> <h2>Implementation</h2>
            To  your symbol recognizers, there are some things you need to consider.
            1. You need to find a way to invoke the recognizer. You can have it run in real time or in
            batch mode (by pressing a button or doing a different, heuristically determined gesture)            
            2. You will need to show recognition results to the user. A simple text box is fine but if you
            want to be more elaborate feel free to do so.
    </li>
    <li> <h2>Deliverables</h2>
            Upload your source code to Canvas. Please include a README file describing what works and
            what does not, the results of your experiments, any known bugs, and any problems you
            encountered
    </li>
    <li> <h2>Grading and Notes</h2>Please include a README file describing what works and
what does not, the results of your experiments, any known bugs, and any problems you
encountered
        80% correct implementation of the recognizers
        20% documentation
    </li>
</ol>

<h1>Successes</h1>
<ol>
    <li> <h2>GitHub</h2>
        This project has been an excellent way to learn and teach myself how to use GitHub. GitHub is an industry standard, and the oppurtunity to become familiar with it is invaluable.
        The convenience of GitHub will allow me to revert any changes I have made to my code which I have taken advantage of plenty of times, and It will also allow me to change development devices with no hassle.
        Over the course of this project I will be out of town and away from my primary development workstation, but my laptop will be able to make use of the repository for seamless development.
    </li>
    <li> <h2>Jet Brains</h2>
        I originally used <a href="https://www.jetbrains.com/clion/download/#section=windows">CLion</a> to develop with C++, but have since switched to JetBrain's <a href="https://www.jetbrains.com/pycharm/download/">PyCharm</a> for development. These have been massive successes and make for easy integration with GitHub, allowing me to push updates to the repository through graphical mouse based interface, and through the command line.
    </li>
    <li> <h2>Markdown Reference</h2>
        The markdown reference guide <a href="https://www.markdownguide.org/basic-syntax/")>here</a> has allowed me to document my readme in style while also empowering this readme to act as a repository for useful links to not only my current and future self, but to anyone who comes across this project in the future. If you want a fancy readme, call it readme.md! Much fancier than readme.me (or even readme.txt)
    </li>
</ol>

<h1>Problems encountered</h1>
<ol>
    <li> <h2>Qt and C++</h2>
            I attempted to use the Qt C++ Library, but it became too unwieldly to implement.
            I would like to implement Qt and take advantage of C++, but based on previous experience 
            with the Qt library I know I would be better suited to deveolping on Linux where Qt plays a little more nicely.
            This diversion would eat into the time necessary to finish the project so I will be abstaining from that.
            Instead I have switched over to Python and the Tkinter library.
    </li>
</ol>

