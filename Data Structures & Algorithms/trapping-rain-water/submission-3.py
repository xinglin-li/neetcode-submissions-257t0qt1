class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        lmax,rmax=0,0
        water=0
        while l<r:
            lh,rh=height[l],height[r]
            if lh<rh:
                if lh<=lmax:
                    water+=lmax-lh
                else:
                    lmax=lh
                l+=1
            else:
                if rh<=rmax:
                    water+=rmax-rh
                else:
                    rmax=rh
                r-=1
        return water
