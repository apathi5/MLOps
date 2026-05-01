function tourImg = calculateTortuosity2D(pointsSorted,geodesicDist,tourImgSize,tstDistance)
% Initialize the touriosity vector and image
tourImg = zeros(tourImgSize);
tour = zeros(size(pointsSorted,1),1);
% Loop through all curve points
    for idx = 1:size(pointsSorted,1)
        % hold the current fixed test point
        curPoint = pointsSorted(idx,:);
        cnt = 1;
        while(true && idx < size(pointsSorted,1))
            %     while(idx < length(rSorted))
            % hold the next tested point
            tstPoint = pointsSorted(idx+cnt,:);
            % Calculate the Euclidean distance
            eclDistance = norm(curPoint-tstPoint);
            % Check if the Euclidean distance satisfies the test distance
            % condition or we reached the end of the curve
            if(eclDistance >= tstDistance || idx+cnt==size(pointsSorted,1))
                % Calculate the touriosity
                tour(idx) = (geodesicDist(idx+cnt) - geodesicDist(idx))/eclDistance;
                % store the touriosity value at the corresponding pixel
                tourImg(pointsSorted(idx,1),pointsSorted(idx,2)) = tour(idx);
                % Exit from the loop and check another pixel
                break;
            end
            % increment the counter to check the next curve point
            cnt = cnt+1;
        end
    end
end
