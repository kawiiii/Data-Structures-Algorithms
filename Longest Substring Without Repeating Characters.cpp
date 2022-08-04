class Solution {
public:
       int lengthOfLongestSubstring(string s) {
        int longest = 0;
        
    for (int i = 0; i < s.length(); i++){
        
        unordered_set<char> letters;
        int tempLongest = 0;
        
        for (int j = i; j< s.length(); j++){
            
            char key = s[j];
            if (letters.find(key) == letters.end()){
                letters.insert(key);
                tempLongest++;
            }
            else
              break;
            if (tempLongest>longest)
                longest= tempLongest;
        }
        
    }
    return longest;
}
       
};
