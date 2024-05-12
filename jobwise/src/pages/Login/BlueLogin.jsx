import React from "react";

const BlueLogin = () => {
  return (
    <div className="container-fluid d-flex justify-content-center vh-100 bg-primary">
      <div className="d-flex justify-content-center flex-column gap-3 text-white">
        <h1>Sign In</h1>
        <form
          className="d-flex flex-column gap-3"
          style={{ minWidth: "350px" }}
          onSubmit={(event) => {
            event.preventDefault();
          }}
        >
          <input
            type="text"
            placeholder="USERNAME"
            className="form-control bg-transparent placeholder-white"
            style={{ minHeight: "50px" }}
          />
          <input
            type="password"
            placeholder="PASSWORD"
            className="form-control bg-transparent placeholder-white"
            style={{ minHeight: "50px" }}
          />
          <div className="d-grid">
            <button className="btn bg-white" style={{ minHeight: "50px" }}>
              Login
            </button>
          </div>
          <a className="text-end text-white" href="#">Forgot password?</a>
        </form>
      </div>
    </div>
  );
};

export default BlueLogin;
