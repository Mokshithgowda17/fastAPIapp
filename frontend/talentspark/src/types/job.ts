interface job {
  id: number;
  title: string;
  salary: number;
  description: string;
  company_id: number;
  jobs: job[];
}
export type { job };