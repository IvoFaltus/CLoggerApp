import "./deepweb.css";

const Deepweb = () => {
  return (
    <div className="dw">
      <div className="dw__panel">
        <div className="dw__header">
          <div>
            <h2 className="dw__title">deepweb dashboard</h2>
            <span className="dw__sub">secure session active</span>
          </div>

          <div className="dw__user">
            <span className="dw__dot" />
            <span>user: ghost_01</span>
            <button className="dw__logout">logout</button>
          </div>
        </div>

        <div className="dw__content">
          <div className="dw__card">
            <h3>messages</h3>
            <p>3 new encrypted messages</p>
            <button className="dw__btn">open inbox</button>
          </div>

          <div className="dw__card">
            <h3>private links</h3>
            <p>12 saved hidden services</p>
            <button className="dw__btn">view links</button>
          </div>

          <div className="dw__card">
            <h3>activity</h3>
            <p>last login: 02:14 UTC</p>
            <button className="dw__btn">details</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Deepweb;