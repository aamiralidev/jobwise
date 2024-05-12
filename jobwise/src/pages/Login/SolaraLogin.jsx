import React from "react";

const SolaraLogin = () => {
  return (
    <div className="container-fluid d-flex align-items-center align-content-center vh-100 w-100">
      <div
        className="d-flex w-100 justify-content-center"
        style={{ maxWidth: "1000px", minHeight: "500px" }}
      >
        <div className="bg-white p-4">
          <h1 className="text-main">Solara</h1>
          <div
            className="p-4 d-flex flex-column gap-3"
            style={{ minWidth: "400px" }}
          >
            <h1 className="fw-bold">Sign In</h1>
            <span>
              Don't have an account?{" "}
              <a className="text-main fw-bold">Create now</a>
            </span>
            <form onSubmit={() => {}} className="d-flex flex-column gap-4">
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
            <button className="btn btn-outline-secondary">
              Continue with Google
            </button>
            <button className="btn btn-outline-secondary">
              Continue with Facebook
            </button>
          </div>
        </div>
        <div className="bg-main" style={{ minWidth: "500px" }}></div>
      </div>
    </div>
  );
};

export default SolaraLogin;
