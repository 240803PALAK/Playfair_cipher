let keystore="";
let matrixstore="";
let ciphertextstore="";
let plaintextstore="";
const plaintext1 = document.getElementById('plaintext').value='';
const key = document.getElementById('key').value='';
const ciphertext1 = document.getElementById('decryptcipher').value='';
const firstRadioButton = document.getElementById("option11");
firstRadioButton.checked = true;
const radioButtons = document.querySelectorAll('input[type="radio"]');
const containers = document.querySelectorAll('.container');
radioButtons.forEach(radioButton => {
  radioButton.addEventListener('change', () => {
    const selectedValue = radioButton.value;
    if (selectedValue==1) {
        const firstRadioButton = document.getElementById("option11");
        firstRadioButton.checked = true;
        document.getElementById('container1').style.display = 'flex';
        document.getElementById('container2').style.display = 'none';
      } else {
        const secondRadioButton = document.getElementById("option22");
        const key = document.getElementById('decryptkey');
        key.innerHTML = keystore;
        secondRadioButton.checked = true;
        document.getElementById('container2').style.display = 'flex';
        document.getElementById('container1').style.display = 'none';
          
      }
  });
});



async function encrypt() {
  const plaintext = document.getElementById('plaintext').value;
  plaintextstore=plaintext;
  const key = document.getElementById('key').value;
  const ciphertext = document.getElementById('ciphertext');

  try {
    const response = await fetch('/encrypt', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        plaintext,
        key
      })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    ciphertext.innerHTML = `${data.ciphertext}`;
    keystore=data.key;
    ciphertextstore=data.ciphertext;
    matrixstore=data.matrix;
  } catch (error) {
    console.error('Error:', error);
  }
}


async function decrypt() {
  console.log(keystore,ciphertextstore,matrixstore)
  const plaintext = document.getElementById('decryptplain');
  const ciphertext = document.getElementById('decryptcipher').value;

  try {
    const response = await fetch('/decrypt', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        ciphertext,
        matrixstore,
        plaintextstore
      })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    plaintext.innerHTML = `${data.plaintext}`;plaintext.innerHTML = `${data.plaintext}`;
  } catch (error) {
    console.error('Error:', error);
  }
}

EncryptBtn.addEventListener('click', encrypt);
DecryptBtn.addEventListener('click', decrypt);

