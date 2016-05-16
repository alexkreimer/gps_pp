dir = '/media/kreimer/0546331841/record_stereo2016_04_17/';
sequences = {'02', '03', '04', '05', '06', '07', '08', '09', '10', '12', '13', '14', '15', '16', '17', '18', '19'};
close all;

for i = 1:length(sequences)
    track_compare(sequences{i}, dir);
end

