---
language:
- en
pipeline_tag: text-classification
widget:
- title: Rating Example
  text: '4.7'
- title: Reviews Example
  text: (188)
- title: Reviews Example 2
  text: '188'
- title: Reviews Example 3
  text: No Reviews
- title: Price Example
  text: $
- title: Type Example
  text: Coffee shop
- title: Address Example
  text: Frederick, MD
- title: Address Example 2
  text: 552 W 48th St
- title: Address Example 3
  text: In Hilton Hotel
- title: Hours Example
  text: Closed
- title: Hours Example 2
  text: Opens 7 AM Fri
- title: Hours Example 3
  text: Permanently closed
- title: Service Option Example
  text: Dine-in
- title: Service Option Example 2
  text: Takeout
- title: Service Option Example 3
  text: Delivery
- title: Phone Example
  text: (301) 000-0000
- title: Years In Business Example
  text: 5+ Years in Business
- title: Button Text Example
  text: Directions
- title: Description Example
  text: 'Provides: Auto maintenance'
license: mit
datasets:
- serpapi/local-results-en
---

<h1 align="center">BERT-Based Classification Model for Google Local Listings</h1>

<p align="center">
  <img src="https://camo.githubusercontent.com/6c920f0b551360ca3257308e0f3547fe538496b9cb332d6a208992030abf6c3d/68747470733a2f2f736572706170692e636f6d2f616e64726f69642d6368726f6d652d353132783531322e706e67" alt="The Logo of SerpApi" width="200" height="200">
</p>

<p align="center">
This repository contains a BERT-based classification model developed using the Hugging Face library, and a dataset gathered by <a href='https://serpapi.com/google-local-api'>SerpApi's Google Local API</a>. The model is designed to classify different texts extracted from Google Local Listings.
</p>

---

<h2 align="center">Usage and Classification for Parsing</h2>

<p align="center">
The example code below represents using it Python with Inference API for prototyping. You may use different programming languages for calling the results, and you may parallelize your work. Prototyping endpoint will have limited amount of calls. For <code>Production Purposes</code> or <code>Large Prototyping Activities</code>, consider setting an <code>Inference API Endpoint from Huggingface</code>, or a <code>Private API Server</code> for serving the model.
</p>

```py
API_URL = "https://api-inference.huggingface.co/models/serpapi/bert-base-local-results"
headers = {"Authorization": "Bearer xxxxx"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": "5540 N Lamar Blvd #12, Austin, TX 78756, United States",
})
```

```
Output: address
```

---

<h2 align="center">Strong Features</h2>

<div align="center">
  <p>The BERT-based model excels in the following areas:</p>
  <div style="display: flex; justify-content: center;">
    <div style="text-align: left;">
      <ul style="list-style-position: inside;">
        <li><strong>Differentiating difficult semantic similarities with ease</strong>
          <ul style="list-style-type: disc;">
            <li><code>"No Reviews"</code> &rarr; <code>reviews</code></li>
            <li><code>"(5K+)"</code> &rarr; <code>reviews</code></li>
          </ul>
        </li>
        <li><strong>Handling partial texts that can be combined later</strong>
          <ul style="list-style-type: disc;">
            <li><code>"Open ⋅ Closes 5 pm"</code>
              <ul style="list-style-type: circle;">
                <li><code>"Open"</code> &rarr; <code>hours</code></li>
                <li><code>"Closes 5 pm"</code> &rarr; <code>hours</code></li>
              </ul>
            </li>
          </ul>
        </li>
        <li><strong>Handling Vocabulary from diverse areas with ease</strong>
          <ul style="list-style-type: disc;">
            <li><code>"Doctor"</code> &rarr; <code>type</code></li>
            <li><code>"Restaurant"</code> &rarr; <code>type</code></li>
          </ul>
        </li>
        <li><strong>Returning Assurance Score for After-Correction</strong>
          <ul style="list-style-type: disc;">
            <li><code>"4.7"</code> &rarr; <code>rating(0.999)</code></li>
          </ul>
        </li>
        <li><strong>Strong Against Grammatical Mistakes</strong>
          <ul style="list-style-type: disc;">
            <li><code>"Krebside Pickup"</code> &rarr; <code>service options</code></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</div>


---

<h2 align="center">Parts Covered and Corresponding Keys in SerpApi Parsers</h2>

  <div style="display: flex; justify-content: center;">
    <div style="text-align: left;">
      <ul style="list-style-position: inside;">
        <li><strong>Type of Place:</strong> <code>type</code></li>
        <li><strong>Number of Reviews:</strong> <code>reviews</code></li>
        <li><strong>Phone Number:</strong> <code>phone</code></li>
        <li><strong>Rating:</strong> <code>rating</code></li>
        <li><strong>Address:</strong> <code>address</code></li>
        <li><strong>Operating Hours:</strong> <code>hours</code></li>
        <li><strong>Description or Descriptive Review:</strong> <code>description</code></li>
        <li><strong>Expensiveness:</strong> <code>expensiveness</code></li>
        <li><strong>Service Options:</strong> <code>service options</code></li>
        <li><strong>Button Text:</strong> <code>links</code></li>
        <li><strong>Years in Business:</strong> <code>years_in_business</code></li>
      </ul>
    </div>
  </div>
</ul>

</div>



<p align="center">
Please refer to the documentation of SerpApi's Google Local API and Google Local Pack API for more details on different parts:
</p>

<div align="center">

<strong>References:</strong>

<ul style="text-align: center; list-style-position: inside;">
  <li>SerpApi's Google Local API: <a href ="https://serpapi.com/google-local-api">https://serpapi.com/google-local-api</a></li>
  <li>SerpApi's Google Local Pack API: <a href="https://serpapi.com/local-pack">https://serpapi.com/local-pack</a></li>
</ul>

</div>

---

<h2 align="center">Known Limitations</h2>

<div align="center">
  <p>The model has a few limitations that should be taken into account:</p>
  <div style="display: flex; justify-content: center;">
    <div style="text-align: left;">
      <ul style="list-style-position: inside;">
        <li>Button text like "Delivery" could be considered <code>service_options</code>. However, this can be easily avoided by checking if a text is in a button in the traditional part of the code. The button text is only used for emergency cases.</li>
        <li>The model does not classify the title of a place. This is because the title often contains many elements that can be easily confused with other parts, even for a human eye.</li>
        <li>The <code>label</code> key is not covered by the model, as it can be easily handled with traditional code.</li>        
        <li>In some cases, the model may classify a portion of the description as <code>hours</code> if the description is about operating hours. For example:
          <ul style="list-style-type: disc;">
            <li><code>"Drive through: Open ⋅ Closes 12 AM"</code>
              <ul style="list-style-type: circle">
                <li><code>"Drive through: Open"</code> &rarr; <code>description</code></li>
                <li><code>"Closes 12 AM"</code> &rarr; <code>hours</code></li>
              </ul>
            </li>
          </ul>
        </li>
        <li>The model may be susceptible to error in one word entries. This is a minority of the cases, and it could be fixed with assurance scores.For Example:
          <ul style="list-style-type: circle">
            <li><code>"Sushi"</code> &rarr; <code>address(0.984), type(0.0493) [Correct Label is type]</code></li>
            <li><code>"Diagorou 4"</code> &rarr; <code>address(0.999) [Correct address in same listing]</code></li>
          </ul>
        </li>
        <li>The model cannot differentiate between extra parts that are extracted in SerpApi's Google Local API and Google Local Pack API. These parts are not feasible to extract via Classification Models.</li>
        <li>The model is not designed for Listings outside English Language.</li>
      </ul>
    </div>
  </div>
</div>

---

<h2 align="center">Disclaimer</h2>

<p align="center">We value full transparency and painful honesty both in our internal and external communications. We believe a world with complete and open transparency is a better world.</p>
<p align="center">
However, while we strive for transparency, there are certain situations where sharing specific datasets may not be feasible or advisable. In the case of the dataset used to train our model, which contains different parts of a Google Local Listing including addresses and phone numbers, we have made a careful decision not to share it. We prioritize the well-being and safety of individuals, and sharing this dataset could potentially cause harm to people whose personal information is included.
</p>
<p align="center">
Protecting the privacy and security of individuals is of utmost importance to us. Disclosing personal information, such as addresses and phone numbers, without proper consent or safeguards could lead to privacy violations, identity theft, harassment, or other forms of misuse. Our commitment to responsible data usage means that we handle sensitive information with great care and take appropriate measures to ensure its protection.
</p>
<p align="center">
While we understand the value of transparency, we also recognize the need to strike a balance between transparency and safeguarding individuals' privacy and security. In this particular case, the potential harm that could result from sharing the dataset outweighs the benefits of complete transparency. By prioritizing privacy, we aim to create a safer and more secure environment for all individuals involved.
</p>
<p align="center">
We appreciate your understanding and support in our commitment to responsible and ethical data practices. If you have any further questions or concerns, please feel free to reach out to us.
</p>