import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>HackMeHome</title>
        <meta name="description" content="Find a mentor to hack with." />
        <link rel="icon" href="/favicon.ico" />
        <script src="./snowstorm.js"></script>
      </Head>

      <main className={styles.main}>
        
        <h1 className={styles.title}>
          Let's start <a>Hacking!</a>
        </h1>

        <p className={styles.description}>
          HackMeHome - A Discord Bot
        </p>

        <div className={styles.grid}>
          <a href="https://discord.gg/G9g3aARmjP" className={styles.card}>
            <h2>Join the Discord server &rarr;</h2>
            <p>We would love for you to join us.</p>
          </a>

          <a href="https://nextjs.org/docs" className={styles.card}>
            <h2>Add to your server &rarr;</h2>
            <p>Add the HackMeHome Bot to your server.</p>
          </a>
        </div>
      </main>

      <footer className={styles.footer}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{' '}
          <span className={styles.logo}>
            <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />
          </span>
        </a>
      </footer>
    </div>
  )
}
