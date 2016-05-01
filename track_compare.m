clear all;
close all;
dbstop if error;
load poses

% read gps locations
data_gt = csvread('data/tr1_data.csv',1);
data_gt = data_gt(:,1:3);
valid = logical(csvread('data/tr1_valid.csv'));

poses(end) = [];
poses = poses(1:10:end);
poses = poses(valid);

valid = true(length(poses),1);
for i = 1:length(poses)
    if isempty(poses{i})
        valid(i) = false;
    end
end

data_gt = data_gt(valid,:);
poses = poses(valid);

data_vo = nan(length(poses),3);
for i = 1:length(poses)
    data_vo(i,:) = poses{i}(1:3,4)';
end

numpts = size(data_vo,1);
[regParams, Bfit, es] = absor(data_vo', data_gt', 'doScale',true, 'doTrans', false);

figure;

data_vo = regParams.s*regParams.R*data_vo'+ repmat(regParams.t, [1 numpts]);
data_gt = data_gt';

plot(data_gt(2,:), data_gt(3,:),'r-');
hold on;
plot(data_vo(2,:), data_vo(3,:),'g-');
legend('DGPS', 'VO');

figure;
plot3(data_gt(1,:), data_gt(2,:), data_gt(3,:),'r-');
hold on;
plot3(data_vo(1,:), data_vo(2,:), data_vo(3,:),'g-');
legend('DGPS', 'VO');

csvwrite('data/vo_data.csv',data_vo');
csvwrite('data/gt_data.csv',data_gt');

regParams