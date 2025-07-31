const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim().split('\n');

function solution(input) {
  const [wordCount, ...words] = input;

  let characters;
  let groupWords = [];

  words.forEach((word) => {
    characters = [];
    let isGroupWord = true;

    if (word.length === 1) {
      groupWords.push(word);
    } else {
      // char 마다 비교하기
      for (let i = 0; i < word.length; i++) {
        const currentCharacter = word[i];
        if (!characters.includes(currentCharacter)) {
          characters.push(currentCharacter);
        } else {
          // 마지막 원소랑 character 가 다르면 그룹 단어가 아니다.
          if (characters[characters.length - 1] !== currentCharacter) {
            isGroupWord = false;
          }
        }
      }

      if (isGroupWord) {
        groupWords.push(word);
      }
    }
  });

  console.log(groupWords.length);
}

solution(input);
