% load('mat_ats9360.mat');
% data0 = Data0{1,3};
% data1 = Data1{1,3};
% save("once_data","data0","data1");
% load('once_data.mat');
% 
% IFreq = 110e6;
% sampleRate = 1.8e9;
% sampleCount = 2048;
% repeatCount = 5000;
% activeCount=1800;
% pSinStandard = zeros(1,1800);
% pCosStandard = zeros(1,1800);
% 
% %本征信号
% for i = 1:activeCount
%     pSinStandard(1,i) = sin(i * 2.0 * pi * IFreq / sampleRate);
% 	pCosStandard(1,i) = cos(i * 2.0 * pi * IFreq / sampleRate);
% end
% 
% %数字解调
% SumSin0 = zeros(5000,1800);
% SumCos0 = zeros(5000,1800);
% SumSin1 = zeros(5000,1800);
% SumCos1 = zeros(5000,1800);
% 
% for i = 1:repeatCount
%     SumSin0(i,:) = data0(i,1:1800).*pSinStandard;
%     SumCos0(i,:) = data0(i,1:1800).*pCosStandard;
%     SumSin1(i,:) = data1(i,1:1800).*pSinStandard;
%     SumCos1(i,:) = data1(i,1:1800).*pCosStandard;
% end
% I0 = SumCos0(:,1);
% Q0 = SumSin0(:,1);
% h = figure;
% hold on;
% grid on;
% scatter(I0,Q0,'b.');
% axis equal;
% hold on;
% grid on;
% scatter(SumSin1(:,2048),SumCos1(:,2048),'r.');
%% 数字下变频不平均
IFreq = 110e6;
sampleRate = 1.8e9;
sampleCount = 2048;
repeatCount = 5000;
activeCount=1980;
load('once_data.mat');

[repeat,Len]=size(data0);
% window = hamming(activeCount);
% window=repmat(window,1,repeat);      %2048个窗函数
t=(1:1:activeCount)./sampleRate;
Seff0=data0(:,1:activeCount);
Seff1=data1(:,1:activeCount);
S_std=exp(-1i*2*pi*IFreq.*t);
S_std=repmat(S_std',1,repeat);
% S1=S_std.*Seff.*window;
S1=S_std.*Seff1';
S0=S_std.*Seff0';
I1=real(S1);
Q1=imag(S1);
I0=real(S0);
Q0=imag(S0);

%% 分段平均
span = 180;       %滑窗大小
slider = 10;      %步长
seg = (activeCount-span)/10+1;            %段数
I1_tr = zeros(seg,5000);
Q1_tr = zeros(seg,5000);
I0_tr = zeros(seg,5000);
Q0_tr = zeros(seg,5000);

for j = 1:slider:(activeCount-span+1)
    I1_tr(fix((j+10)/10),:) = mean(I1((j:j+span-1),:));
    Q1_tr(fix((j+10)/10),:) = mean(Q1((j:j+span-1),:));
    I0_tr(fix((j+10)/10),:) = mean(I0((j:j+span-1),:));
    Q0_tr(fix((j+10)/10),:) = mean(Q0((j:j+span-1),:));
end


%% 平均轨迹
I1_tr_avg = mean(I1_tr');
Q1_tr_avg = mean(Q1_tr');
I0_tr_avg = mean(I0_tr');
Q0_tr_avg = mean(Q0_tr');
figure;
hold on;
grid on;
plot(I0_tr_avg,Q0_tr_avg,'*-',I1_tr_avg,Q1_tr_avg,'*-');
hold on;
grid on;
plot(I0_tr_avg(1),Q0_tr_avg(1),'.','MarkerEdgeColor','b',...
    'MarkerFaceColor',[.49 1 .63],...
    'MarkerSize',30);
plot(I1_tr_avg(1),Q1_tr_avg(1),'.','MarkerEdgeColor','r',...
    'MarkerFaceColor',[.49 1 .63],...
    'MarkerSize',30);

% I_tr1 = I_tr(:,100);
% Q_tr1 = Q_tr(:,100);
