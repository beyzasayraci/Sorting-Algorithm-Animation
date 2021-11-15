function B = counting_sort(A,max_value)
%% Constants
length_array = numel(A);
C = zeros(max_value,1);
%% For Loop
for j = 1:length_array
    C(A(j)) = C(A(j)) +1; %add 1 to index
end

for i = 2:max_value
     C(i) = C(i) + C(i-1); %i index equal to i + i-1 index
    
end
B = nan(length_array,1);

for j = length_array:-1:1
    B(C(A(j))) = A(j);
    C(A(j)) = C(A(j)) -1 ;
end
end
