import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import Snowfall from 'react-snowfall'


export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>HackMeHome</title>
        <meta name="description" content="Find a mentor to hack with." />
        <link rel="icon" href="/favicon.ico" />    
      </Head>

      <div>
      <Snowfall 
        color = "#607d8b"
        snowflakeCount={100}
      />
      </div>

      

      <main className={styles.main}>

        <h1 className={styles.title}>
          Let's start <a>Hacking!</a>
        </h1>

        <p className={styles.description}>
          Want to learn new paradigms? Need help with your current project? 
          Love working on projects and mentoring the next generation?
        </p>  

        <div className={styles.grid}>

          <a href="https://discord.gg/G9g3aARmjP" target = '_blank' className={styles.card}>
            <h2>Join the Discord server &rarr;</h2>
            <p>We would love for you to join us.</p>
          </a>

          <a href="https://discord.com/api/oauth2/authorize?client_id=916667000825217024&permissions=343866018864&scope=bot" target = '_blank' className={styles.card}>
            <h2>Add to your server &rarr;</h2>
            <p>Add the HackMeHome Bot to your server.</p>
          </a>

          <a href="https://github.com/Orectique/HackMeHome" target = '_blank' className={styles.card}>
            <h2>See the project on GitHub &rarr;</h2>
          </a>
        </div>
      </main>
    </div>
    
  )
  
}
