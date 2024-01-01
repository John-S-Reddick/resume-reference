%First I downloaded my dataset from: 
% https://machinelearningmastery.com/standard-machine-learning-datasets/#:~:text=In
% %20this%20post%2C%20you%20will%20discover%2010%20top,the%20expected%20default%20RMSE%20for%20the%20insurance%20dataset.

trainTbl = readtable('winequalityTrain.csv');
testTbl = readtable('winequalityTest.csv');



%%Gaussian
gprMdl = fitrgp(trainTbl,"quality");
ypred = resubPredict(gprMdl);

figure();
plot(trainTbl.quality,'r.');
hold on
plot(ypred,'b');
xlabel('x');
ylabel('y');
legend({'data','predictions'},'Location','Best');
axis([0 4300 0 10]);
hold off;

%%KNN
svmMdl = fitcknn(trainTbl,"quality");
ypred = resubPredict(svmMdl);

figure();
plot(trainTbl.quality,'r.');
hold on
plot(ypred,'b');
xlabel('x');
ylabel('y');
legend({'data','predictions'},'Location','Best');
axis([0 4300 0 10]);
hold off;
ed
