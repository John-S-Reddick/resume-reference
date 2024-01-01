%%

%fitrgp

commandYes   = dir("mini_speech_commands\yes\*.wav");
commandUp    = dir("mini_speech_commands\up\*.wav");
commandStop  = dir("mini_speech_commands\stop\*.wav");
commandRight = dir("mini_speech_commands\right\*.wav");
commandNo    = dir("mini_speech_commands\no\*.wav");
commandLeft  = dir("mini_speech_commands\left\*.wav");
commandGo    = dir("mini_speech_commands\go\*.wav");
commandDown  = dir("mini_speech_commands\down\*.wav");



for i = 1 : length(commandYes)
    t = audioread(commandYes(i).name);
    t = cat(2, t, zeros(16001 - (length(t))));
    t(i, 16001) = 1;
    arr(i) = t;
end

for i = 1001: length(commandUp)
    t = audioread(commandUp(i).name);
    t = cat(2, t, zeros(16001 - (length(t))));
    t(i, 16001) = 2;
    arr(i) = t;
end

for i = 2001 : length(commandStop)
    t = audioread(commandStop(i).name);
    t = cat(2, t, zeros(16001 - (length(t))));
    t(i, 16001) = 3;
    arr(i) = t;
end

for i = 3001 : length(commandRight)
    t = audioread(commandRight(i).name);
    t = cat(2, t, zeros(16001 - (length(t))));
    t(i, 16001) = 4;
    arr(i) = t;
end

for i = 4001 : length(commandNo)
    t = audioread(commandNo(i).name);
    t = cat(2, t, zeros(16001 - (length(t))));
    t(i, 16001) = 5;
    arr(i) = t;
end

for i = 5001 : length(commandLeft)
    t = audioread(commandLeft(i).name);
    t = cat(2, t, zeros(16001 - (length(t))));
    t(i, 16001) = 6;
    arr(i) = t;
end

for i = 6001 : length(commandGo)
    t = audioread(commandGo(i).name);
    t = cat(2, t, zeros(16001 - (length(t))));
    t(i, 16001) = 7;
    arr(i) = t;
end

for i = 7001 : length(commandDown)
    t = audioread(commandDown(i).name);
    t = cat(2, t, zeros(16001 - (length(t))));
    t(i, 16001) = 8;
    arr(i) = t;
end

%%









