import React from "react";

const LeftLogin = () => {
  return (
    <div
      className="container-fluid vh-100 d-flex align-items-center align-content-center"
      style={{ backgroundColor: "#F1F3F6" }}
    >
      <div
        className="w-25 bg-white vh-100 gap-3 d-flex"
        style={{ minWidth: "300px" }}
      >
        <div className="d-flex flex-column justify-content-center align-items-center gap-4 w-100">
          <h1>JobWise</h1>
          <span>Login into your account</span>
          <form
            onSubmit={() => {}}
            className="d-flex flex-column gap-4 w-100 p-3"
            style={{ minWidth: "300px" }}
          >
            <div>
              <label htmlFor="email" className="form-label">
                E-mail
              </label>
              <input
                type="email"
                placeholder="example@gmail.com"
                className="form-control shadow-none"
              />
            </div>
            <div>
              <label htmlFor="password" className="form-label">
                Password
              </label>
              <input
                type="password"
                placeholder="@#*%"
                className="form-control shadow-none"
              />
            </div>
            <div className="d-flex justify-content-between">
              <div class="mb-3 form-check">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="rememberme"
                />
                <label class="form-check-label" for="rememberme">
                  Remember me
                </label>
              </div>
              <a className="text-main fw-bold">Forget Password?</a>
            </div>
            <div className="d-grid">
              <button type="submit" className="btn btn-main text-white">
                Sign in
              </button>
            </div>
          </form>
          <div className="d-flex">
            <hr style={{ width: "45%" }} />{" "}
            <span className="ps-2 pe-2 pt-1">OR</span>
            <hr style={{ width: "48%" }} />
          </div>
          <div className="d-grid w-100 p-3">
            <button className="btn btn-outline-secondary">Signup Now</button>
          </div>
        </div>
      </div>
      <div></div>
    </div>
  );
};

export default LeftLogin;
