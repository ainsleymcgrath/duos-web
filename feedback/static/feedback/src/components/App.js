import React from "react";
import ValidationForm from "./ValidationForm";

export default function App(props) {
  return (
    <div id="app">
      <h2 className="title">
        {props.articleName} by {props.authorName}
      </h2>
      <article className="subtitle">
        In regards to the above, please verify whether the following datasets
        were utilized. If clarifiction is needed, please select that option and
        explain in the text box.
      </article>
      <ValidationForm {...props} />
    </div>
  );
}
