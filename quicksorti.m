
function [arr] = quicksorti(arr,low,high)

if low < high %if last item bigger than first item
     [arr, pivot] = partition(arr, low, high); %call function partition
     arr = quicksorti(arr,low,pivot-1); %recursive calling the itself.
     arr = quicksorti(arr,pivot+1,high); %recursive calling the itself.
     
end

end