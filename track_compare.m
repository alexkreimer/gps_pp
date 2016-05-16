function track_compare(seq, dir)

poses = dlmread(fullfile(dir, 'vo', [seq '.txt']));

% read gps locations
data_gt = csvread(fullfile(dir, 'loc', [seq '.csv']),1);
data_gt = data_gt(:,1:3);
valid = logical(csvread(fullfile(dir, 'loc', [seq '_valid.csv'])));

%poses(end) = [];

poses = poses(1:10:end,:);

n = min(length(valid), length(poses));

poses = poses(1:n,:);
valid = valid(1:n);
poses = poses(valid,:);

n = min(length(poses), length(data_gt));

data_gt = data_gt(1:n, :);
poses = poses(1:n,:);


data_vo = nan(length(poses),3);
for i = 1:length(poses)
    pose = reshape(poses(i,:), [4 3])';
    data_vo(i,:) = pose(1:3,4)';
end

numpts = size(data_vo,1);
[regParams, Bfit, es] = absor(data_vo', data_gt', 'doScale',true, 'doTrans', false);


data_vo = regParams.s*regParams.R*data_vo'+ repmat(regParams.t, [1 numpts]);
data_gt = data_gt';

%figure;
% plot(data_gt(2,:), data_gt(3,:),'r-');
% hold on;
% plot(data_vo(2,:), data_vo(3,:),'g-');
% legend('DGPS', 'VO');

figure;
plot3(data_gt(1,:), data_gt(2,:), data_gt(3,:),'r-');
hold on;
plot3(data_vo(1,:), data_vo(2,:), data_vo(3,:),'g-');
legend('DGPS', 'VO');
title(seq);
export_fig([seq '.png']);
close;

%csvwrite('data/vo_data.csv',data_vo');
%csvwrite('data/gt_data.csv',data_gt');

%regParams