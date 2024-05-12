import React from "react";
import { FcGoogle } from "react-icons/fc";
import { FaFacebook } from "react-icons/fa";
import { BsTwitterX } from "react-icons/bs";

const GreenLogin = () => {
  return (
    <div className="container-fluid d-flex justify-content-center align-content-center vh-100">
      <div
        className="d-flex gap-5 h-auto"
        style={{ maxWidth: "1000px", minHeight: "500px" }}
      >
        <div className="bg-main me-5" style={{ width: "300px" }}></div>
        <div className="bg-white p-4">
          <h1 className="text-main">Solara</h1>
          <div
            className="p-4 d-flex flex-column gap-3"
            style={{ minWidth: "300px" }}
          >
            <h1 className="fw-bold">Sign In</h1>
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
            <span className="text-center">or sign in with</span>
            <div className="d-flex gap-3 justify-content-around">
              <button className="btn btn-outline-main">
                <FcGoogle size={30} />
              </button>
              <button className="btn btn-outline-main">
                <FaFacebook size={30} />
              </button>
              <button className="btn btn-outline-main">
                <BsTwitterX size={30} />
              </button>
            </div>
            <span className="ps-2">
              Don't have an account?{" "}
              <a className="text-main fw-bold">Sign Up</a>
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default GreenLogin;
