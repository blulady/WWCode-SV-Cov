import React, { useContext } from "react";
import { useNavigate } from "react-router-dom";
import { useTeamContext } from "../../context/team/TeamContext";
import ContainerWithNav from "../layout/ContainerWithNav";
import styles from "./Home.module.css";

/*
 * Home page - contains header and Chapter Members link in the body
 */

const Home = () => {
  const navigate = useNavigate();
  const { teams } = useTeamContext();
  let allTeams  = [...teams] || [];
  allTeams.unshift({ id: 0, name: "Chapter Members" });

  const handleClick = (team) => {
    navigate("/members/" + team.toLowerCase().replace(" ", ""));
  };

  return (
    <ContainerWithNav>
      <div className={`${styles["home-container"]} container`}>
        <div className="row">
        {allTeams.map((team) => {
          return (
            <div key={team.id} className={`${styles["home-card"]} ${styles[team.name.toLowerCase().replace(" ", "-")]} col-12 col-md-4`} onClick={() => handleClick(team.name)}>
              <div className={styles.cardimgtop}></div>
              <div className={`${styles.cardbody} d-flex justify-content-center align-items-center`}>
                {team.name}
              </div>
            </div>
          )
        })}
        </div>
      </div>

    </ContainerWithNav>
  );
};

export default Home;
