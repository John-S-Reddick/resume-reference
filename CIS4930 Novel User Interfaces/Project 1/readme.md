Submission: https://canvas.unf.edu/courses/100860/assignments/1328145

Libraries:
  QT Canvas:
    Home:
      https://doc.qt.io/
    Installation:
      https://www.qt.io/offline-installers
      https://www.qt.io/download-qt-installer-oss?utm_referrer=https%3A%2F%2Fwww.qt.io%2Fdownload-open-source


Project 1 – Exploring $-family recognizers
  Due: 2/8/24 11:59 pm

The purpose of this assignment is twofold. It is first designed to give you experience with simple
recognizers using reliable data (touch/stylus/mouse). Second, it is to give you experience with
implementing a state of the art algorithms from scratch by relying on algorithms provided in
the research paper

Requirements:
There are two main requirements for this assignment. First, you will implement 3 $- family
recognizers and compare them. 

The First is the $1 recognizer discussed here:

  PDF of paper
    http://faculty.washington.edu/wobbrock/pubs/uist-07.01.pdf

  Academic source:

The Second recognizer is $Q, details can be found here:

  PDF of paper
    http://faculty.washington.edu/wobbrock/pubs/mobilehci-18.pdf

  Academic source:

The third recognizer is known as Penny Pincher and the details can be found here:

  PDF of paper
    https://www.eecs.ucf.edu/isuelab/publications/pubs/gi2015_eugene.pdf

  https://dl.acm.org/doi/10.1145/3229434.3229465

  Academic citation:
    Taranta, E. and LaViola, J. Penny Pincher: A Blazing Fast, Highly Accurate $-Family Recognizer,
    Proceedings of Graphics Interface 2015, 195-202, June 2015.


You should test these algorithms with the following symbols: 0,1,2,3,4,5,6,7,8,9,+,-,*,t,a,n,s,c,i,
and the square root symbol. I would also recommend adding some more oddball symbols of
your own choosing.

Procedure: 
Train each recognizer with 1, 3, and 5 samples per symbol. Test each recognizer by writing each
symbol 5 times, which should give you a good accuracy number. You should run separate
experiments using the data you collected using a mouse vs a touch screen (if applicable). Please
put the results of your experiment in your README file.

Strategy:
The first step of this project is to create some kind of basic canvas drawing application. This can
be done in any programming language of your choosing, though I recommend looking into the
capabilities of C# with WPF, Python with TK, Java with Swing, or HTML/JS/CSS. No choice is
inherently better than others. You will want to create buttons or widgets to enable the user to
clear the canvas, trigger recognition, and undo previous written strokes. Please see

For Examples of Similar Canvas
https://www.eecs.ucf.edu/isuelab/demo/stochastic-resampling/
https://depts.washington.edu/acelab/proj/dollar/index.html 

implementations which you can work from. Reach out to the instructor if more examples are
needed.

To implement your symbol recognizers, there are some things you need to consider.
  1. You need to find a way to invoke the recognizer. You can have it run in real time or in
  batch mode (by pressing a button or doing a different, heuristically determined gesture)
  2. You will need to show recognition results to the user. A simple text box is fine but if you
  want to be more elaborate feel free to do so.

Deliverables
  Upload your source code to Canvas. Please include a README file describing what works and
  what does not, the results of your experiments, any known bugs, and any problems you
  encountered

Grading will be loosely based on the following:
  80% correct implementation of the recognizers
  20% documentation
